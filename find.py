#!/usr/bin/python3

import argparse
from search import initiate_search
from validate import Validator

def main():
    parser = argparse.ArgumentParser(
        description='This CLI tool searches for words in a specified ' +
        'file using Soundex algorithm.')
    parser.add_argument(
        'filename',
        metavar='filename',
        type=str,
        help='file to be searched in'
        )
    parser.add_argument(
        'word',
        metavar='word',
        type=str,
        help='word to search for'
        )
    args = parser.parse_args()
    validator = Validator()
    validator.is_file_valid(args.filename)
    initiate_search(args.filename, args.word)

if __name__ == '__main__':
    main()
