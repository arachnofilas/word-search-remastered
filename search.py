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
