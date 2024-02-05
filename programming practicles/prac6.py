# Practical Worksheet 6: if statements and for loops
# your name, your number


from graphics import *
import math
from utils import *

#question 1
def fastFoodOrderPrice():
    price = float(input("Price of order: "))
    if price >= 10:
        print("Price + delivery = ", price)
    elif price < 10:
        print("Price + delivery = ", (price + 1.5))

#question 2
def whatToDoToday():
    temp = float(input("Temperature: "))
    if temp > 25:
        print("swim in the sea")
    elif 10 <= temp <= 25:
        print("Go shopping in Gunwharf Quays")
    else:
        print("stay at home and watch a film")


#question 3
def displaySquareRoots(start, end):
    while start <= end:
        print("the square root of", start, "is","{0:0.3f}".format(math.sqrt(start)))
        start += 1

#wuestion 4
def calculateGrade(mark):
    if 16 <= mark <=20:
        return "A"
    elif 12 <= mark <=15:
        return "B"
    elif 8 <= mark <=11:
        return "C"
    elif mark < 8:
        return "F"
    else:
        return "X"

#question 5
def peasInAPod():
    peas = int(input("How many peas: "))
    win = GraphWin("", peas*100, 100)
    for x in range(50, peas*100, 100):
        centre = Point(x,50)
        circle = Circle(centre, 50)
        circle.setFill("Green")
        circle.draw(win)


#question 6
def ticketPrice(distance, age):
    ticket = 3 + (distance * 0.15)
    if age >= 60 or age <=15:
        ticket = ticket * 0.6
    print("Ticket price =  {0:0.2f}".format(ticket))

#question 7
def numberedSquare(n):  
        for i in range(n, 0, -1):
            print(i)
            n += 1
        print("\t")
    #come back to         


# For exercises 8 & 11
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


#question 8
def drawColouredEye(win, centre, radius, colour):
    iris = input("eye colour: ")
    win = GraphWin("", 500, 500)
    centre = Point(250, 250)    
   
    drawCircle(win, centre, 60, "White")
    drawCircle(win, centre, 30, iris)
    drawCircle(win, centre, 15, "Black")

#question 9
def drawPatchWindow():
    win = GraphWin("", 200, 200)
    x = 40
    y = 40
    for i in range(9):
        Lines1 = Line(Point(0, y), Point(x, 0))
        x+=40
        y+=40
        Lines1.setFill("Red")
        Lines1.draw(win)
    for i in range(9):
        Lines2 = Line(Point(x+320, y), Point(x-240, 0))
        x-=40
        y+=40
        Lines2.setFill("Red")
        Lines2.draw(win)   
#similar but not exact
drawPatchWindow()






    
