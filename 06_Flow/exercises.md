# Flow exercises


+ **Write a program to print the numbers from 1 to 10.**

------------


 + **Write a program which asks the user for a number. If number is even print ‘Even’, else print ‘Odd’.**

Getting input from the user can be done using as follows,

```
response = input('enter a number')
response = int(response)
```
--------------
+ **Write a Python program to count the number of even and odd numbers from a series of numbers, provided as a list.**

For example, for the following list ```[1,101,200,50, 25]```, the output would be,

```
even: 2
odd: 3 
```
-----------------
+ **Write a program to check if input number is a prime number.**

A naive solution is to iterate through all numbers from 2 to n-1 and for every number check if it divides n. If we find any number that divides, the number is not a prime.

---------------------

+ **Write a Python program to convert temperatures to and from celsius, fahrenheit.**

Let's assume the user provides the input as a string, with the last character 'c' or 'f', for celsius or fahrenheit. For example, the user could provide ```"20c"```, this would be converted to 68.

The equations are the following:

```
F = 1.8 * C + 32
C = (F - 32) / 1.8
```

--------------------

+ **Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).**

As an extension, make the program stop after it has found 10 numbers.

--------------------

+ **Write a program that allows you to play the scissors rock paper game against the computer.**

	+ Start by writing a program that plays a single round. The user enters their choice using the letters 's', 'r', or 'p'. The computer picks the a random choice and prints out who won.
	+ From this program, extend the program to run forever.
	+ Extend the program to keep a running score. After each round, the scores are printed to the sreen.
	+ Finally, stop the program when one of the players has reached a score of 5. 

--------------------
	
+ **Starting from the code below, count how often each word occurs Moby Dick, ignoring stop words. Print the words occuring more than 250 times.** 
	
```

import nltk
import pandas
import string

nltk.download('gutenberg')
nltk.download('stopwords')

from nltk.corpus import stopwords  

corpus = nltk.corpus.gutenberg.words('melville-moby_dick.txt')
corpus = list(corpus)
corpus = [token.lower() for token in corpus]

unique = set(corpus)

stop_words = list(stopwords.words('english')) + list(string.punctuation) 

```

If you store the words and their counts in the lists ```counts```  and ```words```, you can obtain a sorted version of all words using the following code.

```
frame = pandas.DataFrame({'words':words,'counts':counts})
frame = frame.sort_values('counts', ascending=False)
```

Other texts you can analyse are the following:
```
['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt',
'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt',
'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt',
'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt',
'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt',
'shakespeare-macbeth.txt', 'whitman-leaves.txt']
```