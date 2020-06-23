#!/usr/bin/env python3

#One such usage:
#Let's say I know a router's password is based on the phrase "password"
#python3 phrase_chaser.py password
#hydra -l admin -P pass_list.txt -s 80 -f 192.168.1.1 http-get /

import sys

if len(sys.argv) != 2:
    raise IndexError("Exactly one arg required -- the default phrase to chase.  Exiting..")
phrase = sys.argv[1] 
leet_map = {'O':['0'], 'L':['1', '!'], 'Z':['2'], 'E':['3'], 'A':['4', '@'], 'S':['5', '$'], 'G':['6'], 'T':['7'], 'B':['8']} 

#First things first, we need to get all possible cases for each letter in our phrase
overall_cases = []
for letter in phrase:
    letter_cases = []
    if letter.upper() in leet_map.keys():
        case_set = [letter.lower(), letter.upper()] + leet_map[letter.upper()]
        overall_cases.append(case_set)
    else:
        overall_cases.append([letter.lower(), letter.upper()])

#We will then proceed to combine each possible letters' cases into all expanded possibilities
pass_list = []
def combinator(expression, word, index):
    for case in overall_cases[index]:
        if (len(word) - 1)  > index:
            combinator(expression + case, word, index + 1)
        else:
            pass_list.append(expression + case)
combinator("", phrase, 0)

with open("pass_list.txt", 'w') as plist:
    for password in pass_list:
        plist.write(password + '\n')
