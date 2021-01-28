<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Slicing-and-indexing" data-toc-modified-id="Slicing-and-indexing-1">Slicing and indexing</a></span></li><li><span><a href="#Concatenating-&amp;-Repetition" data-toc-modified-id="Concatenating-&amp;-Repetition-2">Concatenating &amp; Repetition</a></span></li><li><span><a href="#String-methods" data-toc-modified-id="String-methods-3">String methods</a></span></li><li><span><a href="#Converting-from-string-to-number-(and-back)" data-toc-modified-id="Converting-from-string-to-number-(and-back)-4">Converting from string to number (and back)</a></span></li><li><span><a href="#Building-strings-by-concatenation" data-toc-modified-id="Building-strings-by-concatenation-5">Building strings by concatenation</a></span></li><li><span><a href="#Optional:-converting-floats-to-nicely-formatted-text" data-toc-modified-id="Optional:-converting-floats-to-nicely-formatted-text-6">Optional: converting floats to nicely formatted text</a></span></li><li><span><a href="#Exercises" data-toc-modified-id="Exercises-7">Exercises</a></span><ul class="toc-item"><li><span><a href="#Exercise-1:-simple-stuff" data-toc-modified-id="Exercise-1:-simple-stuff-7.1">Exercise 1: simple stuff</a></span></li><li><span><a href="#Exercise-2:-Revisit-old-code" data-toc-modified-id="Exercise-2:-Revisit-old-code-7.2">Exercise 2: Revisit old code</a></span></li><li><span><a href="#Exercise-3" data-toc-modified-id="Exercise-3-7.3">Exercise 3</a></span></li><li><span><a href="#Exercise-4" data-toc-modified-id="Exercise-4-7.4">Exercise 4</a></span></li><li><span><a href="#Exercise-5" data-toc-modified-id="Exercise-5-7.5">Exercise 5</a></span></li><li><span><a href="#Exercise-6" data-toc-modified-id="Exercise-6-7.6">Exercise 6</a></span></li><li><span><a href="#Exercise-7" data-toc-modified-id="Exercise-7-7.7">Exercise 7</a></span></li></ul></li></ul></div>

# Strings

## Slicing and indexing

Strings are used to record textual information. Strings should be considered as a sequence: an ordered collection of characters.

![](https://developers.google.com/edu/python/images/hello.png)

See also here for more information about slicing and indexing strings: https://developers.google.com/edu/python/strings#string-slices



```python
a = 'this is a string'

print(len(a)) #Get the length of string (the number of characters).
print(a[0]) #The first character has index 0
```

    16
    t



```python
print(a[4]) #Spaces are characters as well - this will print a whitespace
```

     



```python
print(a[0:6])
```

    this i



```python
print(a[-1]) # The last item from the end in S
print(a[-2]) # The second-to-last item from the end
```

    g
    n



```python
print(a[1:]) # Everything past the first (1:len(a))
print(a[0:3]) # Three first characters
print(a[:3]) # Same as a[0:3]
print(a[:-1]) # Everything but the last again, but simpler (0:-1)
print(a[:]) # All of a
```

    his is a string
    thi
    thi
    this is a strin
    this is a string


## Concatenating & Repetition

Strings also support concatenation with the plus sign (joining two strings into a new string) and repetition (making a new string by repeating another).


```python
print(a+a)
print(a + " " + a)
```

    this is a stringthis is a string
    this is a string this is a string



```python
print(a*3)
```

    this is a stringthis is a stringthis is a string



```python
print('well, ' + 'this is ' + 'very ' * 3 + 'nice' + '!'*3)
```

    well, this is very very very nice!!!


## String methods

Strings come with a number of neat methods for string manipulations. Below I show a selection of these.

See https://docs.python.org/3/library/stdtypes.html#string-methods for the full documentation.


```python
a.capitalize() #Capitalizes first letter of string
```




    'This is a string'




```python
a.center(20,'*') #Returns a space-padded string with the original string centered to a total of width columns.
```




    '**this is a string**'




```python
a.count('i') #Counts how many times a substring occurs in the string
```




    3




```python
a.endswith('ng') #Determines if string or a substring of string ends with a given suffix
```




    True




```python
a.startswith('string') #Determines if string or a substring of string starts with a given suffix
```




    False




```python
a.isspace() #Returns true if string contains only whitespace characters and false otherwise.
```




    False




```python
a.upper() #Converts the string to upper case
```




    'THIS IS A STRING'




```python
print(a.rstrip(",")) #Removes selected trailing/leading characters
print(a.lstrip('t'))

```

    this is a string
    his is a string



```python
a.replace('string','banana') #replace a substring
```




    'this is a banana'




```python
a.split(' ')
name = 'John,Doe'
print(name.split(','))
```

    ['John', 'Doe']


## Converting from string to number (and back)


```python
# From a float or an integer to a string
a = 10
str(a)
```




    '10'




```python
b = 10.5
str(b)
```




    '10.5'




```python
# The other way around
a = '10'
float(a)
```




    10.0




```python
a = '10'
int(a)
```




    10




```python
# This does not work!
a = '10/.5'
int(a)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-5-4c979d3048b0> in <module>()
          1 # This does not work!
          2 a = '10/.5'
    ----> 3 int(a)
    

    ValueError: invalid literal for int() with base 10: '10/.5'


## Building strings by concatenation

You can build strings, for nicer output, by sticking strings together before printing to the screen. The easiest way is using the `+` sign.


```python
import random
n = random.random()
print('This is a random number: ' + str(n))
```

    This is a random number: 0.5685109014557197



```python
import time
start = time.time()
time.sleep(1.5)
end = time.time()

delta = int((end - start) * 1000)
delta = str(delta)
print("I've slept " + delta + " milliseconds!")
```

    I've slept 1501 milliseconds


## Optional: converting floats to nicely formatted text

Floats can be printed in a nice format by using a formatting string. This describes the 'old' way formatting strings: https://docs.python.org/2/library/stdtypes.html#string-formatting. This old way formatting strings is still the most commonly used one. It's also the most intuitive method. In the interst of completness, this link describes the 'new' way to format strings: https://pyformat.info/.

This is how you build a formating string

+ required:   start sign: %
+ optional:   flag: +, -, 0,
+ optional:   minimum number of characters to use in printing the number
+ required:   the decimal dot
+ required:   number of decimal places
+ required:   the letter `f` to indicate a float is printed


```python
'%05.1f' % 12.3
```




    '012.3'




```python
number = 1245
pct = 99.23

result = (pct * number)/100
print(result)

'%06.2f%% of %.1f is %.1f' % (pct, number, result)
```

    1235.4135





    '099.23% of 1245.0 is 1235.4'



## Exercises

### Exercise 1: simple stuff

+ Write a script that (1) assigns your first name to a variable `v1`, (2) assigns your last name to a variable `v2`, (3) uses `v1` and `v2` to define a variable `v3` listing your complete name, and (4) prints `v3` to screen.
+ Edit the previous script to make sure your name is always printed with capitals.
+ Concatenate your name 10 times with each instance seperated with a space.
+ Convert your name to all caps, assign the result to a new variable.
+ Print a message to the screen saying `The current time is`, followed by the current time and date (use the `time.asctime()` function to get a string stating the current time & date).

### Exercise 2: Revisit old code

Now you know how to work with text, you can use these skills to make the output of your previous scripts nicer.

Write a script that calculates the compounded interest $i$ given a starting capital $p$, an interest rate `r`, and a duration in years $y$. The equation is:

$$i = p \times (1 + r)^y$$

Print out some nicely formatted text. For example


```
5.00 YEAR PROJECTION

Capital:        $2500.00
Rate:           3.00%
Interest:       $398.19
Total:          $2898.19
```

### Exercise 3

Write a short script that does the following:

* Assigns your first name to a variable
* Assigns your family name to a variable
* Creates a new variable containing your initials
* Print that variable to screen

For example, for me (Dieter Vanderelst), the script would print `DV` to screen.

### Exercise 4

Write a script that does the following:

* Assign the text below to a variable.
* Prints out the length of the text.
* Prints out the number of e's in the text.

```
It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.
```

### Exercise 5

Write a script that does the following:

* Assigns a number to a variable, .e.g, `number= 5` .
* Assigns a some drink name to a variable, `drink='soda'` .
* Prints out a variation of the rhyme below where
  * The `x` is replaced by the number in the first variable.
  * `y` is replaced by the drinks name
  * The `z`  is replaced by the number in the first variable, minus 1 (`number-1`).

```
x bottles of y on the wall. x bottles of y. If one of those bottles should happen to fall, z bottles of y on the wall.
```

### Exercise 6

Write a script that assigns a string to a variable `text`. The script swaps the first and the last letter in `text`, and prints the result. For example, for `text='python'`, the script print `nythop`.

### Exercise 7

Write a script that calculates the surface area of a circle from a given diameter. The script prints out the results using the following format (assuming the result of the calculation is 6.23553): 

```
The surface is 6.23553
```

