# Quiz: Intro Pandas

## Question 1

Download the `wages1833.csv` data file (from the data folder) and save it to your computer.

This file contains data on the wages of Lancashire cotton factory workers in 1833.  For each age category, the file lists the following:

* `age`: age in years
* `mnum:` number of male workers of the corresponding age
* `mwage`: average wage of male workers of the corresponding age
* `fnum`: number of female workers of the corresponding age
* `fwage`: average wage of female workers of the corresponding age

More info on the data can be found in this paper:  Boot, H.M. 1995. How Skilled Were the Lancashire Cotton Factory Workers in 1833? Economic History Review 48: 283-303.

Write a script that does the following:

* Read in the data as a pandas dataframe
* Prints the column names
* Prints the first 7 lines of the data
* Adds a new variable that lists the difference between the number of male and female workers
* Adds a new variable ```diff_pct``` that gives the difference in average wage between the male and female workers expressed as a percentage of the female wage. For example, if the average female wage is 90 and the male wage is 135, this new column lists the number 50. In the form of an equation, this gives:

$$
diff_{pct} = 100 \times \frac{(mwage - fwage)}{fwage}
$$



## Question 2

Suppose, I want to read in a file named `data.txt`. The columns of the data are separated by tabs. How can I make sure that pandas reads this data correctly? Complete the blank in the following piece of code:

```python
data = pandas.read_csv('data.txt', _______)
```


## Question 3

Suppose, my data file named `data.csv` has no header (no variable names). How can I read in this file correctly?