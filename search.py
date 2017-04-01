#!/usr/bin/python3

import os
import re
import itertools as it

class FileReader:

    def read_file(self, filename):
        return open(filename, 'r').read().replace(os.linesep, ' ')

    def leave_only_alpha_characters(self, filename):
        new_file = ''
        for word in re.sub('[^a-zA-Z]+', ' ', filename).split():
            new_file += word + ' '
        return new_file

class FileFixer:

    def remove_letters(self, filename):
        remove_ch = 'AEIOUYHW'
        prepared_file = ''
        for word in filename.split():
            word = (word[0] +
                    ''.join(ch for ch in word[1:] if ch.upper() not in remove_ch))
            prepared_file += ''.join(ch for ch, _ in it.groupby(word)) + ' '
        return prepared_file

    def transform_to_soundex(self, word):
        soundex = {'BFPV': '1', 'CGJKQSXZ': '2', 'DT': '3', 'L': '4',
                   'MN': '5', 'R': '6'}
        new_word = ''
        code = ''
        counter = 0
        first_character = word[0]
        for character in word:
            character = character.upper()
            for key in soundex.keys():
                if character in key:
                    dict_number = soundex[key]
                    if not new_word:
                        new_word += dict_number
                        break
                    if dict_number != new_word[-1]:
                        new_word += dict_number
                else:
                    counter += 1
            if counter == 6:
                if not new_word:
                    new_word += character
        new_word = new_word[:4].ljust(4, "0")
        for character in new_word:
            if len(code) < 1:
                code += first_character.upper()
            else:
                code += character
        return code

class SoundComparer:

    def is_similar(self, coded_word, coded_word_from_file):
        if coded_word == coded_word_from_file:
            return True
        elif coded_word[:-1] == coded_word_from_file[:-1]:
            return True
        elif coded_word[:-2] == coded_word_from_file[:-2]:
            return True
        elif coded_word[:-3] == coded_word_from_file[:-3]:
            return True
        else:
            return False

class SimilarListBuilder:

    def append_to_similar_list(self, index, similar, content, similar_words=[]):
        if similar:
            word_in_file = content.split()
            if not similar_words:
                similar_words.append(word_in_file[index])
            if word_in_file[index] not in similar_words:
                similar_words.append(word_in_file[index])
        return similar_words

class Printer:

    def print_similar(self, content):
        if not content:
            print('There are no similar words')
        else:
            print('Similar words in unordered list are:')
        for word in content:
            if len(word) > 1:
                print(word)

def initiate_search(filename, word):
    reader = FileReader()
    fixer = FileFixer()
    comparer = SoundComparer()
    appender = SimilarListBuilder()
    printer = Printer()
    filename = reader.read_file(filename)
    file_content = reader.leave_only_alpha_characters(filename)
    prepared_file = fixer.remove_letters(file_content)
    coded_searched_word = fixer.transform_to_soundex(word)
    for index, word in enumerate(prepared_file.split()):
        coded_word_from_file = fixer.transform_to_soundex(word)
        similar = comparer.is_similar(coded_searched_word, coded_word_from_file)
        similar_words = appender.append_to_similar_list(index, similar, file_content)
    printer.print_similar(similar_words)

if __name__ == '__main__':
    initiate_search()
