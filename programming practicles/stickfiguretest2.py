from graphics import *

def footballPlayer():
    #og code
    win = GraphWin("Stick figure", 300, 200)
    head = Circle(Point(200, 60), 20)
    head.draw(win)
    body = Line(Point(200, 80), Point(200, 120))
    body.draw(win)
    arm1 = Line(Point(200, 90), Point(160, 100))
    arm1.draw(win)
    arm2 = Line(Point(200, 90), Point(240, 100))
    arm2.draw(win)
    leg1 = Line(Point(200, 120), Point(170, 170))
    leg1.draw(win)
    leg2 = Line(Point(200, 120), Point(230, 170))
    leg2.draw(win)
    
    #ground
    ground = Line(Point(0, 170),  Point(300,170))
    ground.draw(win)
    
    #goalpost
    goalPost = Rectangle(Point(60,170), Point(75, 40))
    goalPost.setFill("black")
    goalPost.draw(win)

    #blue football
    football = Circle(Point(160, 155), 15)
    football.setFill("blue")
    football.draw(win)

    #move blue ball
    for i in range(5):
        p = win.getMouse()
        football.move(-25, 0)
        #letters
        
    #this part is incorrect    
    word = "GOAL!"
    for letter in range(0, len(word)):
        x = word[letter]
        y = Text(p, x)
        y.draw(win)
        p.move(10,0)

footballPlayer()

    
