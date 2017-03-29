#!/usr/bin/python3.4

import sys
import os

class Validator:

    def ensureFileIsValid(self):
        try:
            searchedFile = sys.argv[1]
            if os.path.getsize(searchedFile) > 0:
                return open(searchedFile,'r').read().replace(os.linesep, ' ')
                #Validator moved to validate.py and changed files size check
            else:
                print('Imported file is empty')
                sys.exit(1)
        except IndexError:
            print('No file was specified')
            sys.exit(2)
        except FileNotFoundError:
            print('Such file does not exist')
            sys.exit(3)

    def ensureWordIsValid(self):
        try:
            searchedWord = sys.argv[2]
        except IndexError:
            print('No word was specified')
            sys.exit(4)
        return searchedWord
