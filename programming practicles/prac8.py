from graphics import *

class MyPoint():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
    def __str__(self):
        output = "MyPoint({0}, {1})".format(self.x, self.y)
        return output
    def draw(self, win):
        point = Point(self.x, self.y)
        point.draw(win)


class Square():
    def __init__(self, topLeftPoint, sideLength):
        self.fillColour = "black"
        self.p1 = topLeftPoint
        self.side = sideLength
        p2x = self.p1.getX() + sideLength
        p2y = self.p1.getY() + sideLength
        self.p2 = MyPoint(p2x, p2y)
    def getSide(self):
        return self.side
    def getP1(self):
        return self.p1
    def getP2(self):
        return self.p2
    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)
    def __str__(self):
        output = "Square({0}, {1})".format(self.p1, self.side)
        return output
    def setOutline(self, colour):
        self.setOutline = colour
    def getCenter(self):
        p1 = self.p1
        p2 = self.p2
        return Point((p1.x+p2.x)/2.0, (p1.y+p2.y)/2.0)
    def draw(self, win):
        p1 = Point(self.p1.getX(), self.p1.getY())
        p2 = Point(self.p2.getX(), self.p2.getY())
        square = Rectangle(p1, p2)
        square.setFill(self.fillColour)
        square.draw(win)


def testSquare():
    win = GraphWin()
    p1 = MyPoint(100, 50)
    square = Square(p1, 50)
    print(square.getSide())  
    print(square.getP1())  
    print(square.getP2())  
    print(square.getCenter())
    print(square) 
    square.setOutline("blue")
    square.draw(win)
    win.mainloop()
testSquare()


