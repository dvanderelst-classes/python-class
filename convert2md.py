#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 19:26:54 2019

@author: dieter
"""

import glob
import natsort
import os.path as path
import subprocess


file_names = glob.iglob('**/*.ipynb', recursive=True)
file_names = natsort.natsorted(file_names)

for file_name in file_names:
    #parts = path.splitext(file_name)
    #new_file = parts[0] + '.md'
    
    cmd = ["jupyter", "nbconvert", "--to","markdown", file_name]
    state = subprocess.call(cmd)
    print(file_name)
    print(state)