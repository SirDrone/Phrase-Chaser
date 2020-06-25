#!/usr/bin/env python3

#One such usage:
#Let's say I know a router's password is based on the phrase "password"
#python3 phrase_chaser.py password
#hydra -l admin -P pass_list.txt -s 80 -f 192.168.1.1 http-get /

import sys
import argparse

#Do some basic setup: Establish args, create a letter-to-symbol map, etc.
parser = argparse.ArgumentParser(description='Expand a passphrase into its variations')
parser.add_argument('Passphrase', metavar='Passphrase', type=str,
                    help='The passphrase you wish to expand, e.g. kentucky')
restrictive_commands = parser.add_mutually_exclusive_group()
restrictive_commands.add_argument('-a', '--alpha', action="store_true",
               help='Refuse mapping alphabetical characters to symbols/numbers (alphabetical only)')
restrictive_commands.add_argument('-n', '--numerical', action="store_true",
               help='Refuse mapping alphabetical characters to symbols (alphanumerical only)')
parser.add_argument('-s', '--stats', action="store_true",
               help='Gets statistics about a passphrase as opposed to expanding it')
parser.add_argument('-o', '--outfile', type=str, default="pass_list.txt",
               help='Changes the generated output file from pass_list.txt to your choosing')
args = parser.parse_args()
phrase = sys.argv[1] 
if args.numerical:
    leet_map = {'O':['0'], 'I':['1'], 'L':['1'], 'Z':['2'], 'E':['3'], 'A':['4'], 
            'S':['5'], 'G':['6', '9'], 'T':['7'], 'B':['8']} 
else:
    leet_map = {'O':['0'], 'I':['1', '!', '|'], 'L':['1', '!', '|'], 'Z':['2'], 'E':['3'], 'A':['4', '@'], 
            'S':['5', '$'], 'G':['6', '9'], 'T':['7', '+'], 'B':['8'], 'C':['(', '{'], 'X':['%']} 

#If --stats is used, this will help convert bytes to a more human-readable format
def get_simple_measurement(number_of_bytes):
    simple_measure = number_of_bytes
    if (simple_measure / 1024) > 1:
        simple_measure /= 1024
        if (simple_measure / 1024) > 1:
            simple_measure /= 1024
            if (simple_measure / 1024) > 1:
                simple_measure /= 1024
                if (simple_measure / 1024) > 1:
                    return "{} TB".format(round(simple_measure / 1024, 1))
                else:
                    return "{} GB".format(round(simple_measure, 1))
            else:
                return "{} MB".format(round(simple_measure, 1))
        else:
            return "{} KB".format(round(simple_measure, 1))
    else:
        return simple_measure

#First things first, we need to get all possible cases for each letter in our phrase
overall_cases = []
for letter in phrase:
    letter_cases = []
    if not args.alpha and letter.upper() in leet_map.keys():
        case_set = [letter.lower(), letter.upper()] + leet_map[letter.upper()]
        overall_cases.append(case_set)
    else:
        overall_cases.append([letter.lower(), letter.upper()])

#If the user just wanted to know some basic stats for their phrase:
if args.stats:
    number_of_passwords = 1
    for case_set in overall_cases:
        number_of_passwords *= len(case_set)
    number_of_bytes = number_of_passwords * (len(phrase) + 1)
    human_readable_bytes = get_simple_measurement(number_of_bytes)
    print("Number of passwords to be generated: {}\nNumber of potential bytes for {}: {}"
            .format(number_of_passwords, args.outfile, human_readable_bytes))

#Otherwise, we will then proceed to combine each possible letters' cases into all expanded possibilities
else:
    pass_list = []
    def combinator(expression, word, index):
        for case in overall_cases[index]:
            if (len(word) - 1)  > index:
                combinator(expression + case, word, index + 1)
            else:
                pass_list.append(expression + case)
    combinator("", phrase, 0)

    #And output all combinations to our outfile (pass_list.txt by default)
    with open(args.outfile, 'w') as plist:
        for password in pass_list:
            plist.write(password + '\n')
