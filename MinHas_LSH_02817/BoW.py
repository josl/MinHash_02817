#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of MinHas_LSH_02817.
# https://github.com/josl/MinHash_02817

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Jose L. Bellod Cisneros & Kosai Al-Nakeeb
# <bellod.cisneros@gmail.com & kosai@cbs.dtu.dk>
import json
import sys
import re


class BoW():

    def __init__(self, folder):
        self.folder = open(file, 'r')

    def create_bow_from_texts(self, texts, freq_word_dict):
        bow = []
        n_words = len(freq_word_dict)
        for word_index_set in texts:  # go through each text
            words = [0 for i in range(n_words)]  # initialize empty list
            for word in word_index_set:
                words[word] = freq_word_dict[word]  # update indexs with counts
            bow.append(words)
        return bow

    def create_dict_of_texts(self, f):
        texts = []
        word_dict = {}
        index = 0
        pat = re.compile("(\w+)")  # pattern
        for i in json.load(f):  # parse json file
            text_words = i['request_text']
            if text_words == '':
                continue
            words = pat.findall(text_words)  # find words
            text_index = set()
            for word in words:
                if word not in word_dict:  # add unique words
                    text_index.add(index)
                    word_dict[word] = {'index': index, 'count': 1}
                    index += 1
                else:
                    word_dict[word]['count'] += 1
                    text_index.add(word_dict[word]['index'])
            texts.append(text_index)
        freq_word_dict = {}
        for val in word_dict:
            freq_word_dict[word_dict[val]["index"]] = word_dict[val]["count"]
        bow = create_bow_from_texts(texts, freq_word_dict)
        return bow

    def parse_files(self):
        # Walk the tree.
        for root, folder, files in os.walk(self.folder):
            for file_name in files:
                filepath = os.path.join(root, file_name)
                with open(file, 'r') as f:

        bow = create_dict_of_texts(f)
        print(bow)
if __name__ == '__main__':
    main(sys.argv[1])
