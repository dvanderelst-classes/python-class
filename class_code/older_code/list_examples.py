#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:14:28 2021

@author: dieter


"""

############################
## Some examples using random functions on lists
import random

my_list = list(range(0,110))

random.shuffle(my_list)
print(my_list)

c = random.choice(my_list)
print(c)

c = random.sample(my_list,3)
print(c)

print(100 in my_list)

#############################
## List exercise 6

txt = """I travelled for two years in Tibet, therefore, and amused myself by visiting Lhassa,
 and spending some days with the head lama. You may have read of the remarkable
explorations of a Norwegian named Sigerson, but I am sure that it never occurred
to you that you were receiving news of your friend. I then passed through Persia,
looked in at Mecca, and paid a short but interesting visit to the Khalifa at Khartoum
the results of which I have communicated to the Foreign Office. Returning to France,
I spent some months in a research into the coal-tar derivatives, which I conducted in a 
laboratory at Montpellier, in the south of France. Having concluded this to my satisfaction and
 learning that only one of my enemies was now left in London, I was about to return when my movements
 were hastened by the news of this very remarkable Park Lane Mystery, which not 
only appealed to me by its own merits, but which seemed to offer some most peculiar 
personal opportunities. I came over at once to London, called in 
my own person at Baker Street, threw Mrs. Hudson into violent hysterics, and 
found that Mycroft had preserved my rooms and my papers exactly as they had always been.
"""

txt = txt.lower()
txt = txt.replace('.',"")
txt = txt.replace(',',"")
txt = txt.replace('\n',"")
txt = txt.replace('\n\r',"")

words = txt.split(' ')

search_word ='that'

result = words.count(search_word)
print('the word ' + search_word + ' occurs ' + str(result) + ' times')

## exercise 2

import random

my_list = list(range(0, 11))
my_list.remove(3)
my_list.remove(5)
my_list.remove(8)

# solution 1
random.shuffle(my_list)
print(my_list[0])

# solution 2
print(random.choice(my_list))






