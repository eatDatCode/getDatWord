# getDatWord
Python script to grab a quick defintion of the word with a suitable example if any.

(Script uses the https://en.oxforddictionaries.com website to scrap the data.)

# Requirements:
$ pip install -r requirements.txt

# How to setup:
If you are on Windows system, you're on your own to set up the python environment and then use this script.

If you are on Linux or MacOS then it is simple.

Comment out the first statement in getDatWord.py or set it according to your bash( #!/usr/bin/python3.7)

Change the permission to executable 

$ chmod a+x getDatCode.py

# How to Run:
$./getDatCode word(the word you are looking for)

# To access it from anywhere in the terminal:
/*Go to the directory of the git repository */

$ cd getDatWord/

$ cp ./getDatWord.py word

$ sudo mv word /usr/bin/

/* Now the script is available in the terminal from anywhere*/

$ word persuade

Phonetic Spelling:/pəˈsweɪd/

Origin:For a discussion of the difference between persuade and convince, see convince

Persuade(verb):

Definition:Induce (someone) to do something through reasoning or argument.

Example: ‘it wasn't easy, but I persuaded him to do the right thing’

