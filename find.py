#!/usr/bin/python3.4

import sys
import argparse
from validate import Validator
from search import fileReader

class Boss:

    def __init__(self):
        self.validator = Validator()
        self.reader = fileReader()

    def execute(self, filename, word):
        self.validator.ensureFileIsValid(filename)
        myFile = self.reader.readFile(filename)
        print(self.reader.prepareFile(myFile))

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
