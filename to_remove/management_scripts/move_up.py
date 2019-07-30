#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:34:13 2017

@author: dieter
"""

import sys
import os
import glob


def get_folders():
    wd = os.getcwd()
    folders = glob.glob(wd + '/*')
    base_folders = []
    for x in folders:
        base = os.path.split(x)
        base = base[1]
        if '_' in base and os.path.isdir(x) : base_folders.append(base)
    return base_folders

def rename_folder(folder, start, addition):
    split = folder.split('_', 1)
    number = split[0]
    try:
        number = int(number)
        if number >= start: number = str(number + addition)
        number = str(number)
        number = number.zfill(2)
    except:
        pass
    new = number + '_' + split[1]
    return new


values = sys.argv
start = int(values[1])
addition = int(values[2])
folders = get_folders()

for folder in folders:
    new_folder = rename_folder(folder, start, addition)
    print(folder, ' --> ', new_folder)
    os.rename(folder, new_folder)