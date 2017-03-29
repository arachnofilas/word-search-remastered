#!/usr/bin/python3.4

import sys
import os

class Validator:

    def ensureFileIsValid(self, filename):
        try:
            if not os.path.getsize(filename) > 0:
                print('Imported file is empty')
                sys.exit(1)
        except IndexError:
            print('No file was specified')
            sys.exit(2)
        except FileNotFoundError:
            print('Such file does not exist')
            sys.exit(3)
