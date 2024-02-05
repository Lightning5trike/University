import utils
from graphics import *
from utils import *


#og for a square in top left hand
##def main():

##    win = GraphWin("Test", 400, 400)
##    win.getMouse()
##    point = Point(0,0)
##    br = Point(point.x + 100, point.y + 100)
##    rectangle(win, point, br, "blue")
##

##    pause(win)





### EXEC (ENTRY POINT)
##main()



###new
def main():
##    win = GraphWin("Test", 400, 400)
##    colours = ["blue", "green"]
##    centre = Point(x,y)
##    circle = Circle(centre, 50)
    

    #every time you loop moves by 100 in y axis
##    for y in range(0, 400, 100):
##    
##        #every time you loop moves by 100 in x axis
##        for x in range(0, 400, 100):
##            
##            centre = Point(x,y)
##            win.getMouse()            
##            if(x < 200 and y < 200):
##                circle(win, centre, colours[0])
##            elif(x >= 200 and y < 200):
##                circle(win, centre, colours[1])
##            elif(x < 200 and y >= 200):
##                circle(win, centre, colours[1])
##            elif(x >= 200 and y >= 200):
##                circle(win, centre, colours[0])
##            circle.draw(win)
##
##
##    pause(win)



    win = GraphWin("", 400, 400)
    colours = ["blue", "green"]
    for y in range(50, 400, 100):
        for x in range(50, 400, 100):
            centre = Point(x,y)
            win.getMouse()
            circle = Circle(centre, 50)
            if(x < 200 and y < 200):
                circle.draw(win)
                circle.setFill(colours[0])
            elif(x >= 200 and y < 200):
                circle.draw(win)
                circle.setFill(colours[1])
            elif(x < 200 and y >= 200):
                circle.draw(win)
                circle.setFill(colours[1])
            elif(x >= 200 and y >= 200):
                circle.draw(win)
                circle.setFill(colours[0])



# EXEC (ENTRY POINT)
main()
