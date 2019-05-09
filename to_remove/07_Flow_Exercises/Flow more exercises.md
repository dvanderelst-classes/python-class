# Flow: more exercises

## Numbers from 0 to 6

Write a Python program that prints all the numbers from 0 to 6 except 3 and 5.

*Hint*: There are many ways you could write this. One way involves checking  whether a number is not equal to 3 and not equal to 5. Remember, 'Not equal to' is  written as `!=` in Python.

## Buzz and Fizz

Write a Python program which iterates the integers from 1 to 50. For  multiples of three print `Fizz` instead of the number and for the  multiples of five print `Buzz`. For numbers which are multiples of both  three and five print `FizzBuzz`.

*Hint:*`a%b` gives the remainder of a after dividing by b. For example, `7%3` would equal 1. But `6%3` would equal 0.

This is (part of) the required output:

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

## Number guessing game

Write a number guessing game. The program picks a number between 0  and 20. The user is asked to guess the number. For each guess, the  program tells the user whether the guess is too high or to too low. When the user guesses the numbers, the program prints the number of guesses to screen. 

This is an example of the output:

```
Guess:1
Too low
Guess:23
Too high
Guess:234
Too high
Guess:456
Too high
Guess:1
Too low
Guess:12
Too low
Guess:12
Too low
Guess:12
Too low
Guess:12
Too low
Guess:1223
Too high
Guess:10
Too low
Guess:15
Too low
Guess:17
Number of guesses:13
```

## Printing an array of numbers

Write a Python program that takes two digits `m` (row) and `n` (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

For example: 3 and 2, the program prints the following,

```
1 2
2 4
3 6
```

## Minions

Write a program that takes in a text and replaces all words with their minionese counterpart:

https://www.animationsource.org/despicableme/en/custom/&id_film=135&nump=8493

You can use the following piece of code to read in the data in the file `minions.txt`:

```python
dictionary = {}
f = open('minions.txt')
lines = f.readlines()
for x in lines:
    x = x.replace('\n','')
    entry = x.split(',')
    dictionary[entry[1]] = entry[0]
```

## Leap year

******************************************************

Write a program that asks for a year and determines whether it is a leap year.

In the Gregorian calendar three criteria must be taken into account to identify leap years:

+ The year can be evenly divided by 4;
+ If the year can be evenly divided by 100, it is NOT a leap year, unless;
  + The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

