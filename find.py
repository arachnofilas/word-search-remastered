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
        help='Searching specified file'
        )
    parser.add_argument(
        'word',
        metavar='word',
        type=str,
        help='Searching for specified word'
        )
    args = parser.parse_args()
    validator = Validator()
    validator.is_file_valid(args.filename)
    initiate_search(args.filename, args.word)

if __name__ == '__main__':
    main()
