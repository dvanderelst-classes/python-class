
<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Lists-of-lists-(of-lists)" data-toc-modified-id="Lists-of-lists-(of-lists)-1">Lists of lists (of lists)</a></span></li><li><span><a href="#Slicing-&amp;-indexing" data-toc-modified-id="Slicing-&amp;-indexing-2">Slicing &amp; indexing</a></span></li><li><span><a href="#Making-a-list-of-sequential-integers" data-toc-modified-id="Making-a-list-of-sequential-integers-3">Making a list of sequential integers</a></span></li><li><span><a href="#The-Random-module-and-lists" data-toc-modified-id="The-Random-module-and-lists-4">The Random module and lists</a></span></li><li><span><a href="#Check-whether-a-lists-contains-an-item" data-toc-modified-id="Check-whether-a-lists-contains-an-item-5">Check whether a lists contains an item</a></span></li><li><span><a href="#List-methods" data-toc-modified-id="List-methods-6">List methods</a></span><ul class="toc-item"><li><span><a href="#Extending-a-list" data-toc-modified-id="Extending-a-list-6.1">Extending a list</a></span></li><li><span><a href="#Counting-items" data-toc-modified-id="Counting-items-6.2">Counting items</a></span></li><li><span><a href="#Removing-items" data-toc-modified-id="Removing-items-6.3">Removing items</a></span></li><li><span><a href="#Reversing-the-list" data-toc-modified-id="Reversing-the-list-6.4">Reversing the list</a></span></li><li><span><a href="#List-to-string" data-toc-modified-id="List-to-string-6.5">List to string</a></span></li><li><span><a href="#Copying-lists" data-toc-modified-id="Copying-lists-6.6">Copying lists</a></span></li></ul></li><li><span><a href="#Exercises" data-toc-modified-id="Exercises-7">Exercises</a></span><ul class="toc-item"><li><span><a href="#Exercise-1" data-toc-modified-id="Exercise-1-7.1">Exercise 1</a></span></li><li><span><a href="#Exercise-2" data-toc-modified-id="Exercise-2-7.2">Exercise 2</a></span></li><li><span><a href="#Exercise-3" data-toc-modified-id="Exercise-3-7.3">Exercise 3</a></span></li><li><span><a href="#Exercise-4" data-toc-modified-id="Exercise-4-7.4">Exercise 4</a></span></li><li><span><a href="#Exercise-5" data-toc-modified-id="Exercise-5-7.5">Exercise 5</a></span></li><li><span><a href="#Exercise-6" data-toc-modified-id="Exercise-6-7.6">Exercise 6</a></span></li></ul></li></ul></div>

# Lists

The Python list object is the most general sequence provided by the language. Lists are positionally ordered collections of **arbitrarily typed objects**, and they have no fixed size.


```python
import math
a = math.pi
my_list = [1,2,3]
print(my_list)
my_list = [a, '12345', 123, a, a]
print(my_list)
print(len(my_list))
```

    [1, 2, 3]
    [3.141592653589793, '12345', 123, 3.141592653589793, 3.141592653589793]
    5


## Lists of lists (of lists)


```python
lst = [1,2,3]
[lst, my_list, [my_list, lst]]
```




    [[1, 2, 3],
     [3.141592653589793, '12345', 123, 3.141592653589793, 3.141592653589793],
     [[3.141592653589793, '12345', 123, 3.141592653589793, 3.141592653589793],
      [1, 2, 3]]]



## Slicing & indexing

Because they are sequences, lists support all the sequence operations we discussed for strings; the only difference is that the results are usually lists instead of strings.


```python
print(my_list[0])  # Indexing by position
print(my_list[:-1]) # Slicing a list returns a new list
print(my_list + [4, 5, 6]) # Concat/repeat make new lists too
print([1,2,3] * 2)
```

    3.141592653589793
    [3.141592653589793, '12345', 123, 3.141592653589793]
    [3.141592653589793, '12345', 123, 3.141592653589793, 3.141592653589793, 4, 5, 6]
    [1, 2, 3, 1, 2, 3]



```python
my_list[0:1] = [99, 199]
print(my_list)
```

    [99, 199, '12345', 123, 3.141592653589793, 3.141592653589793]


## Making a list of sequential integers


```python
a = range(5)
list(a)
```




    [0, 1, 2, 3, 4]




```python
a = range(7,10)
a = list(a)
a
```




    [7, 8, 9]




```python
a = range(6,12)
a = list(a)
a
```




    [6, 7, 8, 9, 10, 11]



## The Random module and lists


```python
import random
```


```python
my_list = list(range(0,10))
random.shuffle(my_list)
print(my_list)
```

    [7, 4, 6, 0, 9, 2, 3, 8, 5, 1]



```python
my_list = list(range(0,10))
c = random.choice(my_list)
print(c)
```

    8



```python
my_list = list(range(0,10))
c = random.sample(my_list,3)
print(c)
```

    [5, 7, 2]


## Check whether a lists contains an item


```python
a = ['s','p','a','m']
print('p' in a)
print('t' in a)
```

    True
    False


## List methods

Just as strings, strings come with a number of functions that allow manipulating them. Here, I demonstrate a few of them:

### Extending a list


```python
my_list.append('add this') #Add an item to the end of the list
print(my_list)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'add this']



```python
my_list + [1,2,3] # Concatenate lists
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'add this', 1, 2, 3]




```python
b = [1,2,4]
b.insert(2,3) # Insert an item at a specific location
print(b)
```

    [1, 2, 3, 4]


### Counting items


```python
print(my_list)
print(my_list.count('add this')) #Returns count of how many times obj occurs in list
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'add this']
    1



```python
my_list.index(2) #Returns the lowest index in list that obj appears
```




    2



### Removing items


```python
#Items can be removed by index
removed_item = my_list.pop(3)
print(removed_item)
print(my_list)
```

    3
    [0, 1, 2, 4, 5, 6, 7, 8, 9, 'add this']



```python
my_list.remove(9)
print(my_list)
```

    [0, 1, 2, 4, 5, 6, 7, 8, 'add this']


### Reversing the list


```python
my_list.reverse() #Flip the list
print(my_list)
```

    ['add this', 8, 7, 6, 5, 4, 2, 1, 0]


### List to string

*join()* is a string method, **not** a list method. You can’t say **a.join(', ')**, even though it seems more intuitive. The argument to *join()* is a string or any iterable sequence of strings (including a list), and its output is a string.


```python
'_'.join(a)
```




    's_p_a_m'



### Copying lists

When you copy a list, you want to use the explicit `copy()` method.


```python
a = [1,2,3]
b = a.copy()
print(a)
print(b)
```

    [1, 2, 3]
    [1, 2, 3]


Don't use this - I'll explain why in a minute


```python
b = a
print(a)
print(b)
b[0] = '1000'
print(b)
print(a)
```

    [1, 2, 3]
    [1, 2, 3]
    ['1000', 2, 3]
    ['1000', 2, 3]


## Exercises

### Exercise 1

+ Make a list containing (1) your name, (2) the number 3 and (3) the value of $\pi$ (using the math module).
+ Append the boolean value True to the end of the list.
+ Append the boolean value False to the beginning of the list.
+ Create a list containing the numbers 1000 to 2500.
+ Remove the number 1234 from the list.
+ Remove the 1000th entry from the list, and print it.
+ Randomize the order of the numbers in the list.
+ Make a new list containing the first 10 entries in the randomized list.
+ Use the *in* keyword to check whether the value 1000 is in the new list.
+ Replace the third value in the list by the string 'some string'.
+ More: http://www.w3resource.com/python-exercises/list/

### Exercise 2

Create a list of three items (of your choosing) and assign it to a variable.

### Exercise 3

Write a script that, using the list (`var1`) below, does the following:

- Print out the index of the value 2.
- Prints the item with index 3.
- Prints the items with indices 3, 4 and 5.

```python
var1 = [3, 7, 4, 6, 0, 2, 8, 1, 5, 9]
```

### Exercise 4

Write a script that prints out a random number from 0 to 10 (including 0 and 10). However, make sure that the numbers 3, 5 and 8 are never printed.

### Exercise 5

Write a script that generates a list that contains:

* 50 copies of the number 1
* 25 copies of the number 2
* 10 copies of the number 3

Next, shuffle the list and print the index of the first '3' in the shuffled list to the screen.

### Exercise 6

Assign the piece of text below to a variable. Write a script that processes the text:

+ Step 1: Convert the text to lowercase.
+ Step 2: Remove all punctuation (commas and periods).
+ Step 3:  Remove all newline characters (i.e.,`\n`).
+ Step 4: Split the text into a list of individual words (spaces can be used to split the text).
+ Step 5: Your script should be able to a assign a word to a variable, e.g, `search_word ='that'`. The script should print out how many times that word occurs in the text and what the index of its first occurrence is. For the example provided, the script should print 4 and 39.

```
I travelled for two years in Tibet, therefore, and amused myself by visiting Lhassa, and spending some days with the head lama. You may have read of the remarkable explorations of a Norwegian named Sigerson, but I am sure that it never occurred to you that you were receiving news of your friend. I then passed through Persia, looked in at Mecca, and paid a short but interesting visit to the Khalifa at Khartoum the results of which I have communicated to the Foreign Office. Returning to France, I spent some months in a research into the coal-tar derivatives, which I conducted in a laboratory at Montpellier, in the south of France. Having concluded this to my satisfaction and learning that only one of my enemies was now left in London, I was about to return when my movements were hastened by the news of this very remarkable Park Lane Mystery, which not only appealed to me by its own merits, but which seemed to offer some most peculiar personal opportunities. I came over at once to London, called in my own person at Baker Street, threw Mrs. Hudson into violent hysterics, and found that Mycroft had preserved my rooms and my papers exactly as they had always been.
```
