#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: nasmaboumajdi
"""

## setup

from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'treewave',
    version = '0.0.1',
    author = 'Nasma Boumajdi',
    author_email = 'nassma.boumajdi@gmail.com',
    license = 'GNU GPLv3',
    description = 'TreeWave is an open-source, user-friendly command line tool designed for alignment-free phylogeny reconstruction',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = '<github url where the tool code will remain>',
    py_modules = ['treewave', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        treewave=treewave:cli
    '''
)
