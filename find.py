#!/usr/bin/python3

import sys
import argparse
from validate import Validator
from search import fileReader
from search import soundComparer
from search import printer
from search import listCreator
from difflib import SequenceMatcher

class Boss:

    def __init__(self):
        self.validator = Validator()
        self.reader = fileReader()
        self.comparer = soundComparer()
        self.printer = printer()
        self.appender = listCreator()

    def execute(self, filename, word):
        self.validator.ensureFileIsValid(filename)
        filename = self.reader.readFile(filename)
        fileContent = self.reader.removeSymbols(filename)
        preparedFile = self.reader.prepareFile(fileContent)
        codedSearchedWord = self.reader.soundexCode(word)
        for index, word in enumerate(preparedFile.split()):
            codedWordFromFile = self.reader.soundexCode(word)
            similar = self.comparer.isSimilar(codedSearchedWord,codedWordFromFile)
            similarWords = self.appender.appendSimilarList(index,similar,fileContent)
        self.printer.printSimilar(similarWords)

def main():
    parser = argparse.ArgumentParser(description='This CLI tool searches ' +
    'for words in a specified file using Soundex algorithm.')
    parser.add_argument('filename', metavar='filename', type=str,
                        help='file to be searched in')
    parser.add_argument('word', metavar='word', type=str,
                        help='word to search for')
    args=parser.parse_args()
    executor = Boss()
    executor.execute(args.filename,args.word)

if __name__ == '__main__':
    main()
