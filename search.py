#!/usr/bin/python3.4

import os
import re
import itertools as it

class fileReader:

    def readFile(self,filename):
        return open(filename,'r').read().replace(os.linesep, ' ')

    def removeSymbols(self,filename):
        newFile = ''
        for word in re.sub('[^a-zA-Z]+', ' ', filename).split():
            newFile += word + ' '
        return newFile

    def prepareFile(self,filename):
        remove_ch = 'AEIOUYHW'
        preparedFile = ''
        for word in filename.split():
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

class soundComparer:

    def isSimilar(self, codedWord, codedWordFromFile):
        if codedWord == codedWordFromFile:
            return True
        elif codedWord[:-1] == codedWordFromFile[:-1]:
            return True
        elif codedWord[:-2] == codedWordFromFile[:-2]:
            return True
        elif codedWord[:-3] == codedWordFromFile[:-3]:
            return True
        else:
            return False

class printer:

    def printSimilar(self, content):
        print(content)
