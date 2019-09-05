
<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#The-Math-Module" data-toc-modified-id="The-Math-Module-1">The Math Module</a></span><ul class="toc-item"><li><span><a href="#Functions" data-toc-modified-id="Functions-1.1">Functions</a></span></li><li><span><a href="#Constants" data-toc-modified-id="Constants-1.2">Constants</a></span></li></ul></li><li><span><a href="#The-Random-Module" data-toc-modified-id="The-Random-Module-2">The Random Module</a></span></li><li><span><a href="#The-Time-Module" data-toc-modified-id="The-Time-Module-3">The Time Module</a></span><ul class="toc-item"><li><span><a href="#Timing-things" data-toc-modified-id="Timing-things-3.1">Timing things</a></span></li><li><span><a href="#Printing-the-time" data-toc-modified-id="Printing-the-time-3.2">Printing the time</a></span></li></ul></li><li><span><a href="#Your-first-program" data-toc-modified-id="Your-first-program-4">Your first program</a></span></li><li><span><a href="#Exercises" data-toc-modified-id="Exercises-5">Exercises</a></span><ul class="toc-item"><li><span><a href="#Exercise-1" data-toc-modified-id="Exercise-1-5.1">Exercise 1</a></span></li><li><span><a href="#Exercise-2" data-toc-modified-id="Exercise-2-5.2">Exercise 2</a></span></li><li><span><a href="#Exercise-3" data-toc-modified-id="Exercise-3-5.3">Exercise 3</a></span></li><li><span><a href="#Exercise-4" data-toc-modified-id="Exercise-4-5.4">Exercise 4</a></span></li><li><span><a href="#Exercise-5" data-toc-modified-id="Exercise-5-5.5">Exercise 5</a></span></li><li><span><a href="#Exercise-6" data-toc-modified-id="Exercise-6-5.6">Exercise 6</a></span></li></ul></li></ul></div>

# Modules
See `.odp` file for an introduction on modules.


Starting from the concept of a function, we will introduce modules as additional sets of functions. Python comes standard with a large number of modules, listed here: https://docs.python.org/3/py-modindex.html. However, we installed anaconda Python which comes with even more additional modules, listed here: https://docs.continuum.io/anaconda/pkg-docs.

## The Math Module

The Math module is a standard Python module. See https://docs.python.org/3/library/math.html for the complete documentation of the Math module.

### Functions


```python
import math
a = math.sqrt(12355)
a
```




    111.15304764152893




```python
b = math.sin(1)
b
```




    0.8414709848078965



### Constants


```python
p = math.pi
```

## The Random Module

This is another standard Python module. See https://docs.python.org/3/library/random.html for the complete documentation of the Random module.


```python
import random

# a random number between 0 and 1
random.random()
```




    0.9922430817521777




```python
# a random number from a Gaussian distribution
random.gauss(1, 3)
```




    3.1264346377872854



## The Time Module
The `time` module gives access to a number of timing functions. Here, we only cover a few of the things the module can be used for.

### Timing things


```python
import time
```

The function `time()` return the time since an specific reference time and date. This reference point is platform dependent. For Unix, the reference is January 1, 1970, 00:00:00 (UTC). To find out what the epoch is on a given platform, look at `time.gmtime(0)`.


```python
print(time.time())
```

    1567535412.58933



```python
time.gmtime(0)
```




    time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)



Altough the reference point for the `time()` function is arbitrary, we can still use it to measure time.


```python
start = time.time()

(math.pi * math.pi) ** 0.25

completed = time.time()
duration = (completed - start) * 1000 #Take the difference and convert to milliseconds (1/1000th of a second)
print('This took me', duration, 'milliseconds') 
```

    This took me 0.10323524475097656 milliseconds


### Printing the time

The time module has a an easy way to get the current time and date in a standard format (as text).


```python
print(time.asctime())
```

    Thu Sep  6 14:22:48 2018


The module can also be used to print the current time and date in a specified format . The format is a string with placeholders in it. Python will replace these placeholders with the correct values. The place holders you can use are listed here: https://docs.python.org/3/library/time.html#time.strftime


```python
formatting = 'This is the %Wth week of the year. The current month is %B.'
result = time.strftime(formatting)
print(result)
```

    This is the 36th week of the year. The current month is September.


## Your first program

Here we start working with the editor. I'll explain
+ How to enter a script
+ How to save it
+ How to run it

Example script


```python
side = 7
area = side * side
circumference = side * 4
volume = side**3

print(side)
print(area)
print(circumference)
print(volume)
```

    7
    49
    28
    343


## Exercises

### Exercise 1

+ Write a script that assigns a radius to a variable. Next, the script uses this radius to calculate the surface area  or the volume of sphere, using `math.pi`. Print the result to the screen.
+ Write a script that prints the number of remaining days in the year.
+ Print a script that prints out what percentage of the year has passed.

### Exercise 2

+ Write a script that calculates the simple interest $i$ given a starting capital $p$, an interest rate `r`, and a duration in years $y$. The equation is:

$$i = p \times r \times y$$

The interest rate `r` should be entered as a percentage. However, the equation assumes the decimal notation.

+ Expand the previous script to also print out the compounded interest:

$$i = p \times (1 + r)^y$$


+ Suppose we want to develop a game in which a character throws a projectile at the player. The character throws the projectile with a random angle in the range [30-45] degrees and with a speed in the range of [5-10] m/s. Write a script that calculates, for a single throw, how far the projectile travels ($d$) and how long it is airborn ($t$). These are the relevant equations (see https://en.wikipedia.org/wiki/Projectile_motion):

$$ t= \frac{2 v_0 sin(\theta)}{g}$$

$$ d = \frac{v_0^2}{g} \times sin(2\theta)$$



### Exercise 3

What code lets you start using the `math` module?

### Exercise 4

Consult the documentation for the `math` module to answer this question. Write a script that assigns a value to two variables, `var1` and `var2 `and prints out their greatest common divisor?

### Exercise 5

Consult the documentation for the `random` module ([link](https://docs.python.org/3/library/random.html))  to answer this question.

Write a script that does the following:

 * Declares a variable `min_value`.
 * Declares a variable `max_value`.
 * Generates a random number between `min_value` and `max_value`.
 * Assigns this number to a variable, e.g, `random_value`
 * Prints that variable to the screen.

### Exercise 6

Consult the documentation of the `time` module ([link](https://docs.python.org/3/library/time.html)). Write code that prints the current time to the screen in the following format `'It is now 30 minutes past 09'`.
