# Quiz: Functions


## Question 1

Write a function that converts a temperature in degrees celcius into a temperature in degrees Fahrenheit. For example, if your function is called `fahrenheit()`, calling `fahrenheit(-10)` would return `14`.

## Question 2

Write a function that converts a temperature in degrees Fahrenheit into a temperature in degrees Celcius. For example, if your function is called `celcius()`, calling `celcius(14)` would return `-10`.

## Question 3

Use the two functions you made for converting between Celsius and Fahrenheit to make a more complex function. The new function can take a string such as `14F` as input. Using the letter to determine the unit of the input, the function converts the input to the appropriate other unit. For example, `14F` would be converted to `-10C` (and the other way around). 

Hints:

* First, you need to determine whether the input is given in Fahrenheit or Celsius. Also, you need to extract the number from the string. Remember, a string is basically a sequence of characters 
 * You can convert a string to a number using `float(x)`.
* Once you have the units and the number, you can use an `if`-statement to convert the number based on the current unit.
 * Finally, you will need to convert the number into a string and add the unit character (i.e., `F` or `C`).

## Question 4

Use the function you wrote for question 3 to write a function that can take a list of temperatures and convert all of them. For example, if your function is called `convert_list()`, this would be how it is used:

```python
 temperatures=['14F','100F', '20C' ]
 result = convert_all(temperatures)
 print(result)
 >> ['10C', '37C', '68F']
```