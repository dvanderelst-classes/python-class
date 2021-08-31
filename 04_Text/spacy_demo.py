#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 16:58:46 2021

@author: dieter
"""

import spacy
from spacy import displacy
import urllib

url = "https://www.gutenberg.org/files/2852/2852-0.txt"
file = urllib.request.urlopen(url)
text = ''
for line in file:
    decoded_line = line.decode("utf-8")
    text = text + decoded_line
text = text.replace('\r\n', ' ')
for x in range(10): text = text.replace('  ',' ')

    
start = text.find('Chapter 1.')    
end = text.find('Chapter 5.')

text = text[start:end]
    
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

#%%
found_entities = []

current = ''
for token in doc:
    if token.ent_type_ == 'PERSON': 
        if token.ent_iob_ == 'B': print(' ')
        print(token.text, end = ' ')
        
displacy.serve(doc, style="ent")
        
    

    
    
    
        
        
        
        
        


            
             
        
        
     


# https://spacy.io/usage/visualizers
#displacy.serve(doc, style="ent")