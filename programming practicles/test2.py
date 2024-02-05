from graphics import *
import math
from utils import *

def openWindow():
    win = GraphWin("circles", 600, 600)
    count = 0
    colours = ["blue", "pink", "white"]
    while count <=15:
        click = win.getMouse()
        x = click.getX()
        y = click.getY()
        circle = Circle(click, 30)
        if(x < 300 and y < 300):
            circle.setOutline(colours[0])
            circle.setFill(colours[2])
            
        elif(x >= 300 and y < 300):
            circle.setFill(colours[0])
            circle.setOutline(colours[2])
            
        elif(x < 300 and y >= 300):
            circle.setOutline(colours[1])
            circle.setFill(colours[2])
        
            
        else:
            circle.setFill(colours[1])
            circle.setOutline(colours[2])
        circle.draw(win)           
        count+=1

    pause(win)
#openWindow()

def drawCircles2():
    win = GraphWin("circles", 600, 600)
    count = 0
    colours = ["blue", "pink", "white"]
    for y in range(30, 180, 60):
        for x in range(30, 600, 60):
            win.getMouse()
            centre = Point(x,y)
            circle = Circle(centre, 30)
            win.getMouse()
            circle.draw
    
drawCircles2()








    
