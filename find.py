#!/usr/bin/python3.4

from validate import Validator
from search import fileReader

class Boss:

    def __init__(self):
        print('Boss created')

    def execute(self):
        validator = Validator()
        reader = fileReader()
        validator.ensureWordIsValid()
        importedFile = validator.ensureFileIsValid()
        print(reader.prepareFile(importedFile))

if __name__ == '__main__':
    executor = Boss()
    executor.execute()

    '''
    TO DO: check if possible create validator and reader objects in init
    '''
