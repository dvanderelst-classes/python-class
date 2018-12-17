# Quiz: Pandas Filtering

For this quiz, using the following data file: `films.dat` (in the Data folder). This file lists the title, year of release, length in minutes, number of cast members listed, rating, and number of lines of description are recorded for a simple random sample of 100 movies.

## Question 1

Write code to select all films from 1980 to 1990 (including both 1980 and 1990) and assign the result of this operation to a new variable.

## Question 2

Select all films with a rating of 1 and assign the result of this operation to a new variable.

## Question 3

Write a short script that allows selecting all movies that were made in the five years before a given date.

The script starts by assigning a value (year) to a variable. The script selects all movies made in the 5 years preceding the year assigned to the variable and  prints the selected data to the screen. The earliest film in the data was made in 1924. Therefore, if the year assigned to the variable is before 1930, the script should print the message `No movies found`.

## Question 4

Write a script that adds a new variable `ratio` to the data. This variable is obtained by dividing the number of actors (`Cast`) by the length of the movie (`Length`). Next, select the movies for which the ratio Cast/Length is at least 0.1. Print the selected movies to the screen.
