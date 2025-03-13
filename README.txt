-Project: Phrase Chaser
-Version: 1.1
-Author:  SirDrone

#====================================================================================================================

-Purpose:

	To enable penetration testers and home users to evaluate the security of passphrases on authorized devices.

	This project will allow stated entities to expand a passphrase into many possibilities.
	If one knew a phrase was "password", or "melon", but didn't know the exact variations a user may have employed,
	this project will expand those simple phrases into many of their possible derivatives.  It will still work
	on longer phrases, but they will certainly require more time to spin up for, and obviously be harder to crack.

	This project does not intend to be a catch-all to simple phrases, as it is currently* easily defeated by
	adding characters before or after the stated phrase, but it should nonetheless prove useful.

	As a reminder, use this on devices you are expressly permitted to test.  I am not liable for anything you do ;)

#====================================================================================================================

-Files Included:

+phrase_breaker.zip
|
|+++README.txt 
|
|+++LICENSE.txt
|	So no one gets in trouble for using this software :thumbs:
|
|+++phrase_chaser.py
|	The program you'll likely want to run.  Creates a pass_list.txt off the phrase you supply

#====================================================================================================================

-What Is Needed to Run This Program:

	A.  Python3 interpreter in a terminal/shell environment.
	Yep, that's it!  I didn't want anyone to be bogged down by installation, so only basic modules were used.

#====================================================================================================================

-Operating Instructions:

	python3 phrase_chaser.py your_simple_phrase_here

	As mentioned, a pass_list.txt will be created, which you can then plug into a number of brute-force programs.
	You can also evaluate a passphrase's statistics without expanding variations via the --stats option.

#====================================================================================================================

-Changes Since Version 1.0:
	
	1.)  Threw in a few more characters to our symbol translator

	2.)  Provided the option to change the default output file (pass_list.txt) via -o <your_file.txt>
	
	3.)  Added the option to evaluate the potential size of the output file and # of passwords generated.
	This -s (or --stats) option will not create an output file, as phrases won't be chased.

	4.)  Alphanumerical (-n) and alphabetical (-a) only translation restrictions are a thing
	
	5.)  Hello changelog :)

#====================================================================================================================

-Additional Remarks:

	This project currently allows one to both expand and evaluate a passphrase's many variations, though there are
	certainly areas we can improve on.  For instance, when evaluating using the --stats option, both password
	strength and time-to-crack indicators might be nice.  Granted, I'm bearing in mind the expansion of these
	phrases was the point of this simple project, though it is something I may add in a later version.

	I may even work to improve speed, but again, I'm bearing in mind this is for simple phrase cracking.

	Currently, if you'd like to see more on your passphrase's time-to-crack, I highly recommend considering:
	https://github.com/dropbox/zxcvbn
	https://lowe.github.io/tryzxcvbn/

	The Zxcvbn creators put a lot of soul into their work -- I may even integrate it in the future.

	And as before, if you find any bugs or issues, dislike or like this design, please let me know!
	I can only grow with the feedback provided.  Thank you for your time and for using this program.
	Hopefully it proves beneficial

#====================================================================================================================

END
