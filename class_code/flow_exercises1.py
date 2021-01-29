
# Write a program to print the numbers from 1 to 10.

x = 1
while x < 11:
    print(x)
    x = x + 1


for x in range(1, 11):
    print(x)
    
#Write a program which asks the user for a number. If number is even print ‘Even’, else print ‘Odd’.

#response = input('enter a number >')
#response = int(response)

#if response % 2 == 0:
#    print('even')
#else:
#    print('odd')

lst = [1,101,200,50, 25, 124, 44, 566, 778]
odd_count = 0
even_count = 0
for x in lst:
    
    if x % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
    
print(even_count)
print(odd_count)

# Write a program to check if input number is a prime number.

print('------------')
number = 7919

prime = True
for i in range(2, number):
    if number % i == 0:
        prime = False
        break

print(prime)

#
import nltk
import pandas
import string

nltk.download('gutenberg')
nltk.download('stopwords')

from nltk.corpus import stopwords  

corpus = nltk.corpus.gutenberg.words('carroll-alice.txt')
corpus = list(corpus)

corpus = [token.lower() for token in corpus]
unique = set(corpus)
stop_words = list(stopwords.words('english')) + list(string.punctuation) 

counted_words = []
counts = []
for word in unique:
    if word not in stop_words:
        count = corpus.count(word)
        counts.append(count)
        counted_words.append(word)
        
frame = pandas.DataFrame({'words':counted_words,'counts':counts})
frame = frame.sort_values('counts', ascending=False)
    









