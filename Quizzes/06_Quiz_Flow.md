# Quiz: Flow

## Question 1

Write a script that prints out the numbers from 0 to 10. Use the `range()` function.

## Question 2

Write a short script that assigns a value to a variable `var1` and, if the variable is larger than 5, prints `larger than 5`. If the value of `var1` is smaller than 5, the script prints `smaller than 5`.

## Question 3

Write a script that generates random numbers between 0 and 1. This can be be done using the `random()` function in the `random module` (e.g., `var1 = random.random()`). The script keeps generating random numbers until a number smaller than 0.1 is generated. This number is printed to the screen.

## Question 4

Write a script that checks for each number in the range 1000 to 12000 (including both 1000 and 12000) whether the number can be divided by 4. If so, print the number to the screen.

*Hint:  Assuming the number you want to check is in `var1`, checking whether a number can be divided by 4 can be done as follows. :*

```python
var1%4==0
```

This will be `True` if `var1` can be divided by 4. For example, try typing `12%4==0` into the command line. This should return `True`. However, `13%4==0` should return False.

## Question 5

Write a number guessing game. In this game, the computer will try to guess a number you come up with. 

The game starts with you thinking of a number between 0 and 20. Next, the computer tries to guess the number by guessing. After each guess, you are asked to tell whether the computer's guess was too low, too high or correct (use the `input()` function to ask for input from the user). 

Your program should keep track of the highest and lowest possible value of the number you have in mind. For example, if the computer guesses 15 and you tell the computer this is too low, the lowest possible value is 16. Each time, the computer make a guess between the lowest and highest possible number.  

In principle, you could make the program robust against the user cheating (i.e., him or her changing the number during the game). Also, you could make the program more intelligent by making a guess not random but have it lie halfway between the lowest and highest possible value. These extensions are not required for this exercise.

This is example output of such a program:

```text
Is the number 18 ?
l,h,c? -->h
Is the number 1 ?
l,h,c? -->l
Is the number 12 ?
l,h,c? -->h
Is the number 3 ?
l,h,c? -->l
Is the number 9 ?
l,h,c? -->l
Is the number 10 ?
l,h,c? -->l
Is the number 11 ?
l,h,c? -->c
So, the number was 11?
```



