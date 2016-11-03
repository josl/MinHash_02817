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
import os


class BoW():

    def __init__(self, folder):
        self.folder = folder

    def create_bow_from_texts(self, texts, freq_word_dict):
        bow = []
        n_words = len(freq_word_dict)
        for word_index_set in texts:  # go through each text
            words = [0 for i in range(n_words)]  # initialize empty list
            for word in word_index_set:
                words[word] = freq_word_dict[word]  # update indexs with counts
            bow.append(words)
        return bow

    def create_dict_of_texts(self):
        texts = []
        word_dict = {}
        index = 0
        pat = re.compile("(\w+)")  # pattern
        for root, folder, files in os.walk(self.folder):
            print(self.folder)
            for file_name in files:
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r') as f:
                    print(file_path)
                    data_file = json.load(f)  # parse json file
                    for data in data_file:
                        if 'topics' not in data or 'body' not in data:
                            continue
                        text_words = data['body']
                        words = pat.findall(text_words)  # find words
                        text_index = set()
                        for word in words:
                            lower_word = word.lower()
                            if lower_word not in word_dict:  # add unique words
                                text_index.add(index)
                                word_dict[lower_word] = {
                                    'index': index, 'count': 1
                                }
                                index += 1
                            else:
                                word_dict[lower_word]['count'] += 1
                                text_index.add(word_dict[lower_word]['index'])
                        texts.append(text_index)
                        freq_word_dict = {}
                        for val in word_dict:
                            w_count = word_dict[val]["count"]
                            freq_word_dict[word_dict[val]["index"]] = w_count
        self.bow = self.create_bow_from_texts(texts, freq_word_dict)

if __name__ == '__main__':
    # HOWTO:
    # >>> from Hashing import BoW
    # >>> bow = BoW.BoW('tests/dataset/data/full')
    # >>> bow.create_dict_of_texts()
    # >>> len(bow.bow) # BoW stored in bow.bow
    # 10377

    main(sys.argv[1])
