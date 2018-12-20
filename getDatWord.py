#!/usr/bin/python3.7

"""
file: grabDatWord.py
Author: @github.com/eatDatCode
The web dictionary used: https://en.oxforddictoionaries.com/
"""

import sys
import re
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def grabDatWord(word):
    """This methods try to find the input word in the dictionaries definition section
        and returns the needful else diverts to misspell-check method"""
    # Forms a basic search url
    baseUrl = 'https://en.oxforddictionaries.com/'
    url = baseUrl + 'definition/'+ word

    # Scraps the source file for the word and beautifies it
    html = urlopen(url)
    bs = BeautifulSoup(html.read(),'html.parser')
    defList = bs.findAll('span',{'class':'ind'})

    # If the word requested by the user is not found
    if(len(defList)==0):
        # In case the word is slightly misspelled
        print("Checking spelling...")
        spellCheck(baseUrl,word)

    else:
        # Definition/s,associated Part of Speech,Example, Origin, PhoneticSpell
        definedList = bs.findAll('span',{'class':'ind'})
        posList = bs.findAll('span',{'class':'pos'})
        exList = bs.findAll('div',{'class':'ex'})
        origin = bs.findAll('div',{'class':'senseInnerWrapper'})
        phonetic = bs.findAll('span',{'class':'phoneticspelling'})


        l = len(origin[0].get_text())

        # prints the phonetic spelling
        print("Phonetic Spelling:"+phonetic[0].get_text())

        """Boy! sometimes the origin of a word can be a long story so I had to monitor
        the string's length of the origin of a word"""
        if l < 200:
            # prints the origin of the word if it's samll story
            print("Origin:"+origin[0].get_text())

        print("-"*60)

        # Prints definition according to Part Of Speech
        for i in range(len(posList)):
            print(word.capitalize()+"("+posList[i].get_text()+"):")
            print("Definition:"+definedList[0].get_text())
            print("Example:"+exList[i].get_text())
            print("-"*60)



def spellCheck(baseUrl,word):
    """This method try to find the a near match of the misspelled word and gives a suggestion
        or two maybe"""
    # Forms a new url to check near match
    url = baseUrl + 'search?filter=dictionary&query=' + word

    html = urlopen(url)
    # Beautifies the source code
    bs = BeautifulSoup(html.read(),'html.parser')

    # Checks If the word is from Mars <----You get the joke right :)
    nearList = bs.findAll('ul',{'class','search-results'})
    if(len(nearList)==0):
        print("%s NOT FOUND!" % word)
    else:
        # Shows user the list of near matches
        suggestions = bs.findAll('div',{'class':'heading'})
        print("%s is not found,\nHere are some near matches:" % word)

        # Makes a string out of the suggestions
        suggest_string = str(suggestions[0])

        # Forms a regular expression to scraps the suggestions
        regx = re.compile(r'>\w+<')
        suggest_words = regx.findall(suggest_string)

        words = []

        # prints all the suggestions
        l = len(suggest_words) - 2
        for i in range(l):
            print("[%2d] %s" % (i+1,(suggest_words[i][1:-1])))
            words.append(suggest_words[i][1:-1])


        # Prompts user to choose from the list a number
        try:
            choice = int(input('Which one to look for? : '))
        except ValueError:
            print("Enter a number, Not string!")

        if(choice>(l+1)):
            print("Enter a choice lower than the total suggestions Idiot!")

        # Makes another query and redirects to grabDatWord() method
        newWord = words[choice-1]
        print('Looking for %s...' % newWord)
        grabDatWord(newWord)


if __name__=='__main__':

    # Confirms the commmand line word is provided or not
    if(len(sys.argv))==1:
        print("Type the word you are looking for after ./grabDatWord!")
        exit()

    word = sys.argv[1]

    # sends to grabDatWord() method to look for the word
    grabDatWord(word)
