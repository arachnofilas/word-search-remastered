#!/usr/bin/python3.4

import os
import re
import itertools as it

class fileReader:

    def readFile(self,filename):
        return open(filename,'r').read().replace(os.linesep, ' ')

    def prepareFile(self,filename):
        remove_ch = 'AEIOUYHW'
        preparedFile = ''
        for word in re.sub('[^a-zA-Z]+', ' ', filename).split():
            word = (word[0] +
                ''.join(ch for ch in word[1:] if ch.upper() not in remove_ch))
            preparedFile += ''.join(ch for ch, _ in it.groupby(word)) + ' '
        return preparedFile

    def soundexCode(self,word):
        soundex = { 'BFPV': '1', 'CGJKQSXZ': '2', 'DT': '3',
                    'L': '4', 'MN': '5', 'R': '6' }
        newWord=''
        code = ''
        counter = 0
        firstCharacter = word[0]
        for character in word:
            character = character.upper()
            for key in soundex.keys():
                if character in key:
                    dictNumber = soundex[key]
                    if not newWord:
                        newWord += dictNumber
                        break
                    if dictNumber != newWord[-1]:
                        newWord += dictNumber
                else:
                    counter += 1
            if counter == 6:
                if not newWord:
                    newWord += character
        newWord = newWord[:4].ljust(4, "0")
        for character in newWord:
            if len(code) < 1:
                code += firstCharacter.upper()
            else:
                code += character
        return code

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
