#-------------------------------------------------------------------------------
# Practical Worksheet 7: Booleans and while loops
# your name, your number
#-------------------------------------------------------------------------------


from graphics import *
import math
import time



#q1
def getName():
    name = input("what is your name: ")
    while name.isalpha() == False:
        print("incorrect try again")
        name = input("what is your name: ")




# For exercise 2
def trafficLights():
    win = GraphWin()
    rectangle = Rectangle(Point(70, 20), Point(130, 180))
    rectangle.setFill("black")
    rectangle.draw(win)
    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)

    time.sleep(5)
    red.setFill("black")
    amber.setFill("orange")
    time.sleep(5)
    amber.setFill("black")
    green.setFill("green")
    time.sleep(5)
    amber.setFill("orange")
    green.setFill("black")
    time.sleep(5)
    amber.setFill("black")
    green.setFill("black")
    red.setFill("red")
        



        
trafficLights()



# For exercise 6
def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32








#q5
def clickableEye():
    win = GraphWin("", 500, 500)
    centre = Point(250, 250)

    #from prac 6
    def drawCircle(win, centre, radius, colour):
        circle = Circle(centre, radius)
        circle.setFill(colour)
        circle.setWidth(2)
        circle.draw(win)


    drawCircle(win, centre, 60, "White")
    drawCircle(win, centre, 30, "brown")
    drawCircle(win, centre, 15, "Black")

    click = win.getMouse()

    #from prac 5
    #could just call the function
    x1 = int(click.getX())
    x2 = 250
    y1 = int(click.getY())
    y2 = 250
    squared = ((x2-x1)**2) + ((y2-y1)**2)
    dist = math.sqrt(squared)

    
    if 30 < dist < 60:
        text = Text(Point(100, 100), "sclera")
    elif 15 < dist < 30:
        text = Text(Point(100, 100), "iris")
    elif 0 < dist < 15:
        text = Text(Point(100, 100), "pupil")
    else:
        text = Text(Point(100, 100), "random area")
    text.draw(win)


