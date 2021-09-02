#
# THIS IS THE CODE FOR THE MICROBIT EXERCISES WE DID IN CLASS
#

# blinking an LED, whenever button A is pressed

while True:
    if input.button_is_pressed(Button.A):
        led.plot(3, 1)
        basic.pause(100)
        led.unplot(3, 1)
        basic.pause(100)

# blinking all LEDs, whenever button A is pressed
 while True:
    if input.button_is_pressed(Button.A):
        led.plot_all()
        basic.pause(10)
        basic.clear_screen()
        basic.pause(10)

# this code waits for the button to be released before 
# switching on the LED. This code mimicks approaches to 
# detect a single button press in different kinds of devices
while True:
    led.unplot(0, 0)
    if input.button_is_pressed(Button.A):
        while input.button_is_pressed(Button.A): basic.pause(100)
        led.plot(0, 0)
        basic.pause(1000)

# pressing button A rotates the arrow to the next position

counter = 0
basic.show_arrow(ArrowNames.NORTH)
while True:
    if input.button_is_pressed(Button.A):
        while input.button_is_pressed(Button.A): basic.pause(100)
        counter = counter + 1
        if counter > 7: counter = 0
        if counter == 0:  basic.show_arrow(ArrowNames.NORTH)
        if counter == 1:  basic.show_arrow(ArrowNames.NORTH_EAST)
        if counter == 2:  basic.show_arrow(ArrowNames.EAST)
        if counter == 3:  basic.show_arrow(ArrowNames.SOUTH_EAST)
        if counter == 4:  basic.show_arrow(ArrowNames.SOUTH)
        if counter == 5:  basic.show_arrow(ArrowNames.SOUTH_WEST)
        if counter == 6:  basic.show_arrow(ArrowNames.WEST)
        if counter == 7:  basic.show_arrow(ArrowNames.NORTH_WEST)

# Now with reset button

counter = 0
basic.show_arrow(ArrowNames.NORTH)
while True:
    if input.button_is_pressed(Button.A):
        while input.button_is_pressed(Button.A): basic.pause(100)
        counter = counter + 1
        if counter > 7: counter = 0
        if counter == 0:  basic.show_arrow(ArrowNames.NORTH)
        if counter == 1:  basic.show_arrow(ArrowNames.NORTH_EAST)
        if counter == 2:  basic.show_arrow(ArrowNames.EAST)
        if counter == 3:  basic.show_arrow(ArrowNames.SOUTH_EAST)
        if counter == 4:  basic.show_arrow(ArrowNames.SOUTH)
        if counter == 5:  basic.show_arrow(ArrowNames.SOUTH_WEST)
        if counter == 6:  basic.show_arrow(ArrowNames.WEST)
        if counter == 7:  basic.show_arrow(ArrowNames.NORTH_WEST)

    if input.button_is_pressed(Button.B):
        while input.button_is_pressed(Button.B): basic.pause(100)
        counter = 0
        basic.show_arrow(ArrowNames.NORTH)


