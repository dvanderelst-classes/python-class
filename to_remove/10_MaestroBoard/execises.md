# Maestroboard

+ Make the green LEDs switch off and on for 10 times at a rate of 1 Hz. Finally, switch on the red LED.
+ Print `Who turned off the lights?` to screen each time the photocell is blocked.
+ Turn the green led on if the photocell is not blocked. Turn the red led on each time the photocell is blocked.
+ Make a counter using the photocell: count how many times the light is blocked and print the number to the screen. Stop the loop when you have counted ten blocking events.
+ Write a script that turns servo 1 as you turn the dial of the potentiometer. When the photocell is blocked, the loop is stopped.
+ Make a quiz response timer. Let’s say a quiz allows x seconds to think about your answer. Use one of the servos to count down the time from x to zero. Once the time is up, the red light switches on. The candidate can press the response button to answer by touching the photocell. Write a program that sets one of the motors to positions between 0 and 1 in ten steps. Wait one second between steps.
+ Write a program that sets one of the motors to positions between 0 and 1 in ten steps. Wait one second between steps.
+ Write a program that keeps checking the position of the dial. If the dial position is smaller than 0.5, turn on the red LED. Else, turn on the green LED. Use `dial = b.get_pot().`
+ Modify this program such that the position of one of motors follows the position of the dial.
+ Write a program that uses one of the motors as a dial showing the light level.
+ Write a program that allows you to use the dial to select a light level below which the LEDs will be turned on. You can use one motor to give feedback to the user about the selected light level. The other motor can be used to display the actual light level.
