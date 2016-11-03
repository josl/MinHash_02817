#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of MinHas_LSH_02817.
# https://github.com/josl/MinHash_02817

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Jose L. Bellod Cisneros & Kosai Al-Nakeeb
# <bellod.cisneros@gmail.com & kosai@cbs.dtu.dk>

from Hashing import MinHash
from Hashing import BoW


def main():
    # This shoud be imported from the root folder of the repo
    # >>> from Hashing import ex1
    # >>> ex1.main()
    bow = BoW.BoW('tests/dataset/data/full')
    bow.create_dict_of_texts()
    rows = len(bow.bow)  # bag of words stored in bow.bow
    columns = len(bow.bow[1])
    # BoW = Matrix of 10377 x 28473
    # Columns might be wrong... from the exercise:
    #
    # How many features/columns do you get in your term/document matrix from
    # your bag-of-words encoding? One solution (mine) gives a matrix of size
    # 10377 x 70794 (this is without removing punctuation)

if __name__ == '__main__':
    main()
