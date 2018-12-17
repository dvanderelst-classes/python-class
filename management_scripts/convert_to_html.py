#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:34:13 2017

@author: dieter
"""


import os
import natsort
import glob
import shutil
import subprocess
import markup

def get_folders():
    wd = os.getcwd()
    folders = glob.glob(wd + '/*')
    selected_folders = []
    for x in folders:
        base = os.path.split(x)
        base = base[1]
        if '_' in base and os.path.isdir(x) : selected_folders.append(x)
    selected_folders  = natsort.natsorted(selected_folders)
    return  selected_folders


def get_folder_number(folder):
    base = os.path.split(folder)
    base = base[1]
    base = base.split('_', 1)
    number = base[0]
    name = base[1]
    return number, name

def get_notebooks(folder):
    keywords = ['prepare', 'preparation', 'quiz', 'excercise']
    selected = []
    files = glob.glob(folder + '/*.ipynb')
    for filename in files:
        triggered = False
        for kw in keywords: 
            if kw in filename.lower(): triggered = True
        if not triggered: selected.append(filename)
    return selected

def convert_single(file_name):
    args = ['jupyter','nbconvert', '--allow-errors', '--to', 'html_embed', '--execute']
    args.append(file_name)
    output, error = run(args)
    new_file = file_name.replace('.ipynb','.html')
    return new_file, output, error


def run(args):
    #subprocess.check_call(args)
    df = subprocess.Popen(args, stdout=subprocess.PIPE)
    output, error = df.communicate()
    return output, error
    

def convert_notebooks(folder):
    wd = os.getcwd()
    files = get_notebooks(folder)
    print(files)
    folder_number, folder_base = get_folder_number(folder)
    counter = 0
    html_files = []
    for notebook in files:
        suffix = ''
        if len(files) > 1: suffix = str(counter).zfill(2)       
        new_file, output, error = convert_single(notebook)
        new_file_name = folder_number + '_' + folder_base + suffix + '.html'
        new_location = wd + '/html/' + new_file_name
        shutil.move(new_file, new_location)
        print('>>>>>> ', new_location)
        counter+=1
        html_files.append(new_file_name)
    return html_files
  

folders = get_folders()
page = markup.page()
page.init()
page.br()
for fld in folders:
    print(fld)
    files = convert_notebooks(fld)
    for x in files:
        text = x.replace('.html','')
        text = text.replace('_', ' ')
        page.a(text, class_='internal', href=x)
        page.br()

f = open('html/index.html','w')
f.write(str(page))
f.close()
    
