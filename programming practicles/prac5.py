# Practical Worksheet 5: Using functions

from graphics import *
import math


# For exercises 1 and 2
def areaOfCircle(radius):
    return math.pi * radius ** 2


# For exercise 3
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


# For exercise 5
def drawBrownEye(win, centre, radius):
    drawCircle(win, centre, 60, "White")
    drawCircle(win, centre, 30, "Brown")
    drawCircle(win, centre, 15, "Black")
    

#question 1
def circumferenceOfCircle(radius):
    return math.pi * radius * 2

#question 2
def circleInfo():
    radius = int(input("radius: "))
    print("The are is", "{0:0.3f}".format(areaOfCircle(radius)) ,"and the circumference is", "{0:0.3f}".format(circumferenceOfCircle(radius)))

#question 3
def drawBrownEyeInCentre():
    win = GraphWin()
    drawCircle(win, Point(250,250), 60, "White")
    drawCircle(win, Point(250,250), 30, "Brown")
    drawCircle(win, Point(250,250), 15, "Black")


#question 4
def drawBlockOfStars(width, height):
    count = 0
    while count < height:
        print('*' * width)
        count += 1

#question 4 continued
def drawLetterE():
    print(drawBlockOfStars(8, 2))
    print(drawBlockOfStars(2, 2))
    print(drawBlockOfStars(8, 2))
    print(drawBlockOfStars(2, 2))
    print(drawBlockOfStars(8, 2))

#come back to technically functions but there is a none inbetween each print statement



#question 5
def drawPairOfBrownEyes():
    win = GraphWin("", 500, 500)
    centre = Point(190, 250)
    drawBrownEye(win, centre, 100)
    centre = Point(310, 250)
    drawBrownEye(win, centre, 100)


#question 6
def distanceBetweenPoints(p1, p2):
    x1 = int(p1.getX())
    x2 = int(p2.getX())
    y1 = int(p1.getY())
    y2 = int(p2.getY())
    squared = ((x2-x1)**2) + ((y2-y1)**2)
    dist = math.sqrt(squared)
    print("distance: {0:0.3f}".format(dist))

#question 7
def drawBlocks(width, width2, width3, width4, width5):
    count = 0
    while count < 3:
        print(' ' * width, '*' * width2, ' ' * width3, '*' * width4, ' ' * width5)
        count += 1

#question 8
def drawFourPairsOfEyes():
    win = GraphWin("", 500, 500)
    p1 = win.getMouse()
    drawPairOfBrownEyes()
#come back to this


#question 9
    
#win = GraphWin("", 500, 500)
#spacing = 40
def displayTextWithSpaces(win, spacing, size, phrase, p):
    p = Point(100, 250)
    for letter in range(0, len(phrase)):
        a = phrase[letter]
        b = Text(p, a)
        b.setSize(size)
        b.draw(win)
        p.move(spacing,0)
#displayTextWithSpaces(win, 40, int(input("font size: ")), input("phrase: "))

        
def constructVisionChart():
    win = GraphWin("", 500, 500)
    displayTextWithSpaces(win, 10, 30, input("phrase: "), Point(235, 60))
    displayTextWithSpaces(win, 20, 25, input("phrase: "), Point(215, 100))
    displayTextWithSpaces(win, 30, 20, input("phrase: "), Point(195, 140))
    displayTextWithSpaces(win, 25, 15, input("phrase: "), Point(175, 180))
    displayTextWithSpaces(win, 25, 10, input("phrase: "), Point(155, 200))
    displayTextWithSpaces(win, 10, 5, input("phrase: "), Point(115, 240))


#question 10

def drawStickFigure(win, point, size):
    win = GraphWin("Stick figure")
    point = win.getMouse()
    x = point.getX()
    y = point.getY()
    
    head = Circle(Point(x,y), 20)
    head.draw(win)
    body = Line(Point(0, y+20), Point(x+0, y+60))
    body.draw(win)
    arms = Line(Point(x+30, y+35), Point(x+30, y+35))
    arms.draw(win)
    leg1 = Line(Point(x+30, y+95), Point(x+0, y+60))
    leg1.draw(win)
    leg2 = Line(Point(x+30, y+95), Point(x+0, y+60))
    leg2.draw(win)

def drawStickFigureFamily():
    pass
#finish later
