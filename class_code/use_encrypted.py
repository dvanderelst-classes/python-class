#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:30:44 2019

@author: dieter
"""

import encrypt

message = "A multitude of people and yet a solitude"
key = 'dickens'

encrypted = encrypt.encrypt(message, key)
print(encrypted)


