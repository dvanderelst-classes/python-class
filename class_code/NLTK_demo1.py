#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 17:23:21 2021

@author: dieter
"""
import urllib
import string
import nltk
import collections
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk import pos_tag


#nltk.download('punkt')
#nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')


url = 'https://www.gutenberg.org/cache/epub/16370/pg16370.txt'
file = urllib.request.urlopen(url)
text = ''
for line in file:
    decoded_line = line.decode("utf-8")
    text = text + decoded_line
text = text.replace('\r\n', ' ')
for x in range(10): text = text.replace('  ',' ')




#%% Pos tagging and lemmatization

wnl = WordNetLemmatizer()
sentences = sent_tokenize(text)
current_sentence = sentences[150]
tokens = word_tokenize(current_sentence)
tagged = pos_tag(tokens)

print(current_sentence)
for x in tagged:
    word = x[0]
    tag = x[1]
    if x[1].startswith('V'):
        result = wnl.lemmatize(word, pos='v')
        print(word, tag, result)
        
        
#%% Get all the adjectives in the text
all_adjectives = []
for current_sentence in sentences:
    tokens = word_tokenize(current_sentence)
    tagged = pos_tag(tokens)
    for x in tagged: 
        word = x[0]
        tag = x[1]
        if x[1].startswith('J'):
            result = wnl.lemmatize(word, pos='a')
            #print(word, tag, result)
            all_adjectives.append(result)
        
#%% Count the number of unique adjectives and the length of the text
occurrences = collections. Counter(all_adjectives)
print(occurrences)
a = len(occurrences)
b = len(word_tokenize(text))

c = a/b
print(a)
print(b)
print(c)


        
        