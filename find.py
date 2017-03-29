#!/usr/bin/python3.4

import sys
import os

class Validator:

    def isValidFile(searchedFile):
        try:
            searchedFile = sys.argv[1]
            with open(searchedFile,'r') as importedFile:
                fileContent = importedFile.read().replace(os.linesep, ' ')
                if not fileContent:
                    print('Imported file is empty')
                    sys.exit(1)
                return fileContent
        except IndexError:
            print('No file was specified')
            sys.exit(2)
        except FileNotFoundError:
            print('Such file does not exist')
            sys.exit(3)

    def isValidWord(searchedWord):
        try:
            searchedWord = sys.argv[2]
        except IndexError:
            print('No word was specified')
            sys.exit(4)
        return searchedWord

if __name__ == '__main__':
    validator = Validator()
    importedFile = validator.isValidFile()
    searchedWord = validator.isValidWord()
    print(importedFile)
    print(searchedWord)
