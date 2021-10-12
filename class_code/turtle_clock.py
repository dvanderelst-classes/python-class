import time
import datetime
import turtle				# import the turtle module
turtle.bye()				# close existing screens, if any

my_turtle = turtle.Turtle()	# make a variable called robot
my_turtle.shape('turtle')		

while True:
    
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute
    if hours > 12: hours = hours - 12
    
    #hours = 4
    #minutes = 0
    
    angle_hours =  - (hours - 3) * 30     
    angle_minutes =  - (minutes - 15) * 6
    
    print(angle_hours, angle_minutes)
    
    turtle.clearscreen()
    
    my_turtle = turtle.Turtle()	
    my_turtle.shape('turtle')		
    
    for h in range(12):
          indicator_angle =  - (h - 3) * 30
          my_turtle.setheading(indicator_angle)
          my_turtle.pu()
          my_turtle.fd(200)
          my_turtle.pd()
          my_turtle.pensize(3)
          my_turtle.pencolor('red')
          my_turtle.fd(20)
          my_turtle.pu()
          my_turtle.home()
         
        
    my_turtle.pencolor('black')
    my_turtle.setheading(angle_hours)
    my_turtle.pensize(10)
    my_turtle.pd()
    my_turtle.fd(100)
    my_turtle.pu()
    
    my_turtle.home()
    
    my_turtle.setheading(angle_minutes)
    my_turtle.pd()
    my_turtle.pensize(5)
    my_turtle.fd(150)
    
    time.sleep(10)
    my_turtle.pu()
        
