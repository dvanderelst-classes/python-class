#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 14:30:15 2018

@author: dieter
"""
import urllib
from matplotlib import pyplot

def encrypt(plaintext, keyword):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_alphabet = alphabet
    for letter in keyword:
        cipher_alphabet = cipher_alphabet.replace(letter,'')
    cipher_alphabet = keyword + cipher_alphabet
    # Step 2: encrypt
    encrypted_text = ''
    for letter in plaintext:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            letter = cipher_alphabet[letter_index]
        encrypted_text = encrypted_text + letter
    return encrypted_text, cipher_alphabet

link = 'https://tinyurl.com/yd4pugor'
f = urllib.request.urlopen(link)
txt = f.read()
txt = str(txt)
start = txt.find('One morning')
end = txt.find('End of the Project')
txt = txt[start:end]

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Count the letters in the original text
counts = []
for letter in alphabet:
    count = txt.count(letter)
    counts.append(count)
# plot the histogram
pyplot.bar(range(0,26),counts)
pyplot.xticks(range(0,26), list(alphabet))

txt,cipher_alphabet = encrypt(txt, 'zebra')

# Count the letters in the encrypted
counts = []
for letter in alphabet:
    count = txt.count(letter)
    counts.append(count)

# plot the histogram
pyplot.figure()
pyplot.bar(range(0,26),counts)
pyplot.xticks(range(0,26), list(alphabet))










