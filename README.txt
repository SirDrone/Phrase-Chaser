-Project: Phrase Chaser
-Version: 1.0
-Author:  ***REMOVED***

#====================================================================================================================

-Purpose:

	To enable penetration testers and home users to evaluate the security of passphrases on authorized devices.

	This project will allow stated entities to expand a phrase into many possibilities.
	If one knew a phrase was "password", or "melon", but didn't know the exact variations a user may have employed,
	this project will expand those simple phrases into many of their possibile derivatives.  It will still work
	on longer phrases, but they will certainly require more time to spin up for, and obviously harder to crack.

	This project does not intend to be a catch-all to simple phrases, as it is currently* easily defeated by
	adding characters before or after the stated phrase, but it should nonetheless prove useful.

	As a reminder, use this on devices you are expressly permitted to test.  I am not liable for anything you do ;)

#====================================================================================================================

-Files Included:

+phrase_breaker.zip
|
|+++README.txt (or README.pdf if you prefer bolding!)
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

#====================================================================================================================

-Additional Remarks:

	This is my second publicly released project.

	Right now, it doesn't do many fancy things, though in the next version, I plan to both:
	-Allow the user to more easily control the name of the output file
	-Provide a "count" argument for the user to see how many passwords/bytes would be generated before use

	I may even work to improve speed, but again, I'm bearing in mind this is for simple phrase cracking.

	And as before, if you find any bugs or issues, dislike or like this design, please let me know!
	I can only grow with the feedback provided.  Thank you for your time and for using this program.
	Hopefully it proves beneficial

#====================================================================================================================

END
