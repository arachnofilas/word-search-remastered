#!/usr/bin/python3.4

import re
import itertools

class fileReader:

    def prepareFile(self,importedFile):
    #Function which removes adjacent and non alphabetical characters
        preparedFile = ''
        for word in re.sub('[^a-zA-Z]+', ' ', importedFile).split():
            preparedFile += ''.join(ch for ch, _ in itertools.groupby(word)) + ' '
        return preparedFile

    '''
    def readSingleWord(importedFile):
        for line in importedFile:
            for word in line.split():
                print(word)
    '''

#class soundComparer:

#class printer:


    '''
    PUT INTO find.py ?????:


    with open('wiki_lt.txt','r') as f:
        for line in f:
            for word in line.split():
                print(word)

        def clearRemovableLetters(wordList):
            removable_letters = 'aeiouyhw'
            newWordList = []
            for word in wordList:
                newWord = (word[0] +
                    ''.join(ch for ch in word[1:] if ch not in removable_letters))
                    newWordList.append(newWord)
            return newWordList
    '''
