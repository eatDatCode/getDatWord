#!/usr/bin/python3.7
"""
file: dict.py
author: @github.com/eatDatCode
Takes a single word as command line argument and gives
Definition with example
"""

import re
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getDatWord(word):
    """This method search for the word in dictionay.com and returns \
            the definition with a suitable example"""
    # This string forms the url from which the data will be scrapped
    url = 'https://www.dictionary.com/browse/'+word+'?s/t'

    # Uses the library urllib and scraps the source code of the url
    html = urlopen(url)

    # Beautifies the html source code using BeautifulSoup library
    bs = BeautifulSoup(html.read(),'html.parser')

    # Find all the tags where the definition is in dictionary.com
    wordLine = bs.findAll('li',{'value':'1'})

    # Checks If word not found in the dictionary.com
    if( len(wordLine) == 0):
        print("Word %s not found!\t Make sure you spelled it right." % word)
        exit()

    # Seperate the definition and example
    defRegx = re.compile(r'.+:')
    exampleRegx = re.compile(r':.+')
    definitionData = wordLine[0].get_text()

    definition = defRegx.findall(definitionData)
    example = exampleRegx.findall(definitionData)

    # Check whether there is an example or not
    if(len(example) == 0):
        definition = definitionData[:-1]
        example = "---"
    else:
        definition = definition[0][:-1]
        example = example[0][2:]

    # Sends the dat to printWord methods to be printed
    printWord(definition,example)


def printWord(defn,exmpl):
    """This method simply prints the word definition and example \
            by formatting the strings"""
    print("Definition: %s." % defn.capitalize())
    print("Example: %s " % exmpl.capitalize())


if __name__=='__main__':
    """ This method initiates the program , taking input from command line\
            then calling the getDatWord() method to give output"""
    # If user don't give commnad line argument then print error!
    if(len(sys.argv) == 1):
        print("Error! Type a word after the script.")
        print("e.g: ./getDatWord hello")
        exit()

    # Assigns the argument to word variable
    word = sys.argv[1]

    # Calls the method to find the word definition
    getDatWord(word)
