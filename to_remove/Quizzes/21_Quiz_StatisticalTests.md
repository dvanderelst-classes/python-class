# Quiz: Statistical Tests

Use the file `Wages.csv` for this quiz. This data contains 3294 observations on wages, experience and gender from 1976 to 1982 in the US. 

Variables:

- `exper`: experience in years
- `sex`: a factor with levels (male,female)
- `school`: years of schooling
- `wage`: wage (in 1980) $ per hour

## Question 1

Write a script that does the following:

- Read in the data.
- Calculate the average wage per each level of years of schooling
- Create a graph that plots the average wage as a function of the years of schooling. Add labels to the axes.
- Run  a linear regression with years of schooling as the independent variable  and wage as dependent variable. Print the summary to the screen.

## Question 2

Write code to run a linear regression with

- the variables `school` and `exper` as independent variables
- the variable `wage` as dependent variable.

## Question 3

Write code running two Kruskal-Wallis H-tests for independent samples:

+ Test 1: Compare the level of experience for males and females.
+ Test 2: Compare the wages for males and females.