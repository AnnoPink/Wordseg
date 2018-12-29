#！/usr/bin/env python
# -*- coding:UTF-8 -*-
# Last modified: 2018/12/29

"""
    docstring
"""

import sys
import pdb

def load_test_data(f):
    sentences=[]
    with open(f) as fd:
        for line_num, line in enumerate(fd):
            ll=line.strip("\n\r").split("  ")

            print(ll)

test_file="data/135.txt"
t=load_test_data(test_file)