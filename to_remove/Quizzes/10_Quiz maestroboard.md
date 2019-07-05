# Quiz: maestroboard

## Question 1

Write a script that, every 10 seconds, records the current light level. The recorded light levels are stored in a list. Every time the script records a new value, it prints the current date and time. For example:

``` 
Data recorded at Sun Jul 29 16:09:20 2018: 0.176
```

The script should define a variable, e.g. `num_of_measurments`, that gives the number of measurements that should be taken. For example, if ``num_of_measurments= 100`, the script should take 100 measurements.

## Question 2

Write a number guessing game that uses the board the give feedback to the player. The script starts by selecting a random number `target` between 1 and 20. The player has to guess this number in the fewest attempts. The script ask the player to make a guess. If the guess is too low, the script turns on the red LED. If the guess is too high, the green LED is turned on. If the player guesses correctly, both LEDs should blink 3 times. The script also prints out the number of guesses.

## Question 3

Write a script that uses the board as a reaction timer. The script waits until the light sensor is blocked. Next, the script waits a random number of seconds before switching on the LEDs. As soon as the LEDs come on, the user should, as quickly as possible remove his/her finger from the sensor. The script measures the time between switching on the LEDs and the removal of the finger from the light sensor.