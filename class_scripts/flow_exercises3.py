#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:21:23 2018

@author: dieter
"""

var1 = 10

if var1%2==0:
    print('even')
else:
    print('odd')
    
    
for var1 in range(1000,1501):
    if var1%3==0:
        print(var1)
        
roman = [
[ 'M',  1000 ], [ 'CM',  900 ],
[ 'D',   500 ], [ 'CD',  400 ],
[ 'C',   100 ], [ 'XC',   90 ],
[ 'L',    50 ], [ 'XL',   40 ],
[ 'X',    10 ], [ 'IX',    9 ],
[ 'V',     5 ], [ 'IV',    4 ],
[ 'I',     1 ]
]


var1 = 250
roman_string = ''

for sublist in roman:
    letter = sublist[0]
    value = sublist[1]
    while var1 >= value:
        roman_string = roman_string + letter
        var1 = var1 - value
print(roman_string)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
plaintext = 'the money is in the safe'
keyword = 'zebra'

# Step 1: cipher alphabet



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

print(encrypted_text)

# Step 3:

decrypted_text = ''
for letter in encrypted_text:
    if letter in alphabet:
        letter_index = cipher_alphabet.index(letter)
        letter = alphabet[letter_index]
    decrypted_text = decrypted_text + letter
    
print(decrypted_text)







