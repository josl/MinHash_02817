#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of MinHas_LSH_02817.
# https://github.com/josl/MinHash_02817

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Jose L. Bellod Cisneros & Kosai Al-Nakeeb
# <bellod.cisneros@gmail.com & kosai@cbs.dtu.dk>

from setuptools import setup, find_packages
from MinHas_LSH_02817 import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='MinHas_LSH_02817',
    version=__version__,
    description='Computational tools for Big Data (02807) - MinHas & LSH',
    long_description='''
Computational tools for Big Data (02807) - MinHas & LSH
''',
    keywords='',
    author='Jose L. Bellod Cisneros & Kosai Al-Nakeeb',
    author_email='bellod.cisneros@gmail.com & kosai@cbs.dtu.dk',
    url='https://github.com/josl/MinHash_02817',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'MinHas_LSH_02817=MinHas_LSH_02817.cli:main',
        ],
    },
)
