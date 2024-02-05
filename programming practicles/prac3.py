# Practical Worksheet P3: Graphical Programming
# your name, your number

from graphics import *
import math

##
###opening the graphics window
##win = GraphWin()
###set the size of the window
##p = Point(30,40)
###accessor methods to get coordinates (done in terminal)
###p.getX()
###p.getY()
###mutator methods change the state of the object somehow
##p.draw(win)
###z.move(x,y)can also be done terminal
##p.move(20, 10)
###to change the colour
##p.setOutline("blue")
##q = Point(100, 70)
##q.draw(win)
##q.setOutline("red")




###lines shapes and text
##win = GraphWin()
###setting the centre point
##centre = Point(100,100)
###20 is the radius
##circle1 = Circle(centre, 20)
###to display the circle inside of the window
##circle1.draw(win)
###width (self explanatory)
##circle1.setWidth(3)
##circle1.setOutline("cyan")
##
##circle2 = Circle(Point(30, 30), 10)
##circle2.draw(win)
##circle2.setFill("green")
##circle2.move(10, 20)
###check the radius (done in terminal)
###circle2.getRadius()



###how to draw a line
##win = GraphWin()
##line = Line(Point(20, 25), Point(30, 60))
##line.draw(win)
##line.move(0, 50)
##line.setOutline("pink")
##
###how to draw a rectangle
###define where top left and bottom right point are
##win = GraphWin()
##rectangle = Rectangle(Point(10,30), Point(40, 100))
##rectangle.draw(win)
##rectangle.setFill("black")
##
###how to draw other types of shapes (polygons)
###list the points
###e.g. triangle
##win = GraphWin()
##triangle = Polygon(Point(100, 20), Point(120, 80), Point(140, 10))
##triangle.draw(win)
##triangle.setFill("yellow")


###text
###centre point followed by the string you want to write
##win = GraphWin()
##text = Text(Point(100, 100), "Hello World")
##text.draw(win)
##text.setSize(20)
##text.setTextColor("magenta")
##text.setText("Goodbye")

###name of window and the dimensions
##win = GraphWin("My Window", 330, 160)
###or you can use regular coordinates instead of pixels
##win.setCoords(0, 0, 1, 1)
###and then you could use float value based coordinates for other things
###e.g.
##line = Line(Point(0, 0.25), Point(1, 0.25))
##line.draw(win)

##obtains the coordinates of where the user clicked their mouse
##win = GraphWin("Click Me!")
##p = win.getMouse()
##print(p.getX(), p.getY())
##p.draw(win)

##def practice():
##     win = GraphWin("Greeter", 400, 300)
##     message = Text(Point(200, 100), "Enter your name & click mouse")
##     message.draw(win)
##     inputBox = Entry(Point(200, 200), 10)
##     inputBox.draw(win)
##     win.getMouse()
##     message.setText("Hello, " + inputBox.getText())
##
##practice()

##

## general programming exercises


def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    #question 1
    arms = Line(Point(70, 95), Point(130, 95))
    arms.draw(win)
    leg1 = Line(Point(70, 155), Point(100,120))
    leg1.draw(win)
    leg2 = Line(Point(130, 155), Point(100,120))
    leg2.draw(win)

#question 2
def drawCircle():
    radius = float(input("radius: "))
    centre = Point(100,100)
    win = GraphWin("question 2")
    circle = Circle(centre, radius)
    circle.draw(win)




#question 3
def drawArcheryTarget():
    centre = Point(100,100)
    win = GraphWin("archeryTarget")
    circle2 = Circle(centre, 30)
    circle2.draw(win)
    circle2.setFill("blue")
    
    circle3 = Circle(centre, 20)
    circle3.draw(win)
    circle3.setFill("red")

    circle1 = Circle(centre, 10)
    circle1.draw(win)
    circle1.setFill("yellow")
    
#question 4
def drawRectangle():
    win = GraphWin("drawRectangle", 200, 200)
    height = float(input("height: "))
    width = float(input("width: "))
    bl = (200 - width)/2
    tl = (200 - height)/2
    rectangle = Rectangle(Point(bl, tl), Point((200-bl), (200-tl)))
    rectangle.draw(win)


#question 5
def blueCircle():
    win = GraphWin("blueCircle")
    p = win.getMouse()
    x = p.getX()
    y = p.getY()

    circle = Circle(Point(x, y), 50)
    circle.draw(win)
    circle.setFill("blue")


#question 6
def drawLine():
    win = GraphWin("Line drawer")
    for i in range(10):
        message = Text(Point(100,100), "Click on first point")
        message.draw(win)
        p1 = win.getMouse()
        message.setText("Click on second point")
        p2 = win.getMouse()
        line = Line(p1, p2)
        line.draw(win)
        message.setText("")

        
#question 7
def tenStrings():
    win = GraphWin("tenStrings", 500, 500)
    for i in range(10):
        p = win.getMouse()
        x = p.getX()
        y = p.getY()
        inputBox = Entry(Point(x, y), 10)
        inputBox.draw(win)
        

#question 8
def tenColouredRectangles():
    win = GraphWin("tenColouredRectangles", 750, 750)
    for i in range(10):
        #add in placeholder of blue for the colour
        inputBox = Entry(Point(375, 50), 20)
        inputBox.draw(win)
        p1 = win.getMouse()
        p2 = win.getMouse()
        rectangle = Rectangle(p1, p2)
        rectangle.setFill(inputBox.getText())
        rectangle.draw(win)
        
        
#question 9
def fiveClickStickFigure():
    win = GraphWin("Stick figure" , 400, 400)
    p1 = win.getMouse()
    x1 = p1.getX()
    y1 = p1.getY()
    
    p2 = win.getMouse()
    x2 = p2.getX()
    y2 = p2.getY()
    pythagoras = math.sqrt((x2-x1)**2+(y2-y1)**2)
    
    head = Circle((p1), (pythagoras))
    head.draw(win)

    p3 = win.getMouse()
    y3 = p3.getY()
    
    body = Line(Point(x1, y3), Point(x1, (x1-pythagoras)))
    body.draw(win)
    
    p4 = win.getMouse()
    x4 = p4.getX()
    y4 = p4.getY()
    
    arms = Line(Point(x4, y4), Point((400-x4), y4))
    arms.draw(win)
    
    p5 = win.getMouse()
    x5 = p5.getX()
    y5 = p5.getY()

    leg1 = Line(p5, p3)
    leg1.draw(win)
    leg2 = Line(Point((400-x5), y5), (p3))
    leg2.draw(win)

#get back to it but it does technically function


#question 10
def plotRainfall():
    win = GraphWin("plotRainfall", 520, 440)
    xAxis = Line(Point(80, 360), Point(80, 80))
    xAxis.draw(win)
    yAxis = Line(Point(80, 360), Point(440, 360))
    yAxis.draw(win)

    inputBox = Entry(Point(400, 40), 10)
    inputBox.draw(win)

    rectangleM = Rectangle(Point(80, 80), Point(inputBox.getText, 120))
    rectangleM.draw(win)

plotRainfall()









    

