from graphics import *

# FUNCTIONS


def myCircle(win,centre,radius,colour):
    c = Circle(centre,radius)
    c.setFill(colour)
    c.draw(win)


def myRectangle(win, tlPoint, brPoint, colour):
    r = Rectangle(tlPoint,brPoint)
    r.setFill(colour)
    r.draw(win)


##my code for triangle
def myTriangle(win, p1, p2, p3, colour):
    t = Polygon(p1, p2, p3)
    t. setFill(colour)
    t.draw(win)
##


def print10():
    print("-" * 10)


def menu():
    print10()
    print("-- MENU --")
    print10()
    print("Select an option")
    print("1 - circle")
    print("2 - rect")
    print("3 - triangle")
    print10()
    return int(input("please select an option: "))


# ENTRY POINT
def main():
    selection = menu()
    win = GraphWin("", 500, 500)
    if selection == 1:
        centre = Point(250, 250)
        radius = int(input("radius: "))
        colour = "Blue"
        myCircle(win, centre, radius, colour)
    elif selection == 2:
        tlPoint = Point(250, 250)
        brPoint = Point(300, 400)
        colour = "Green"
        myRectangle(win, tlPoint, brPoint, colour)
    elif selection == 3:
        p1 = Point(150,200)
        p2 = Point(400, 400)
        p3 = Point(150, 400)
        colour = "Red"
        myTriangle(win, p1, p2, p3, colour)
    else:
        print10()
        

# EXEC (ENTRY POINT)
main()
