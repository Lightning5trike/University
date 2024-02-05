from graphics import *
from utils import *


colours = ["red", "green", "blue", "purple", "orange", "cyan"]
chosenColour = []

while len(chosenColour) < 3:
   colour = input("colour " + str(len(chosenColour) + 1) + ": ")
   if colour in colours:
      chosenColour.append(colour)
   else:
      print("invalid")


patchSize = int(input("patchsize (either 5 or 7): "))
while patchSize != 5 and patchSize != 7:
   print("retry")
   patchSize = int(input("size: "))
patchSize = patchSize * 100


win = GraphWin("patches", patchSize, patchSize)

#code to make the colours of the patches
def patchColouring(x, y, patchSize):
      global colour
      global chosenColour
      patchMod2 = patchSize // 2

      if (x >= patchMod2 and y <= (patchMod2 - 100)) or (x <= (patchMod2 - 100)and y >= (patchMod2)):
         colour = chosenColour[1]
      elif x >= patchMod2 and y >= (patchMod2) or (x <= (patchMod2 - 100) and y <= (patchMod2 - 100)):
         colour =chosenColour[0]
      else:
         colour = chosenColour[2]
         
#penultimate patch/crosses d and e referenced later make it so that it moves by 100 into the line the patches it needs to go in
def patchP(win, d, e, colour):
   x = 0
   y = 100
   for i in range(6):
      line(win, Point(x + d, 100 + e), Point(100 + d, x + e), colour)
      x += 20
   for i in range(5):
      y -= 20
      line(win, Point(y + d, e), Point(d, y + e), colour)
   #had to reset the variables because they got changed within the if statement
   x = 0
   y = 100
   for i in range(5):
      line(win, Point(x + d, e), Point(100 + d, y + e), colour)
      x += 20
      y -= 20
   # x and y are switched as they are just variables and have switched places numerically
   for i in range(6):
      line(win, Point(y + d, 100 + e), Point(d, x + e), colour)
      x -= 20
      y += 20

#final patch/ triangle patch a and b have the same functionality as d and e in patchP
def patchF(win, a, b, colour):  
   for y in range(0, 100, 40):
      for x in range(0, 100, 20):
         triangle1 = triangle(win, Point((x + a), (y + 20 + b)), Point((x + a + 10), (y + b)), Point((x + 20 + a), (y + 20 + b)), colour)

   for y in range(0, 60, 40):
      for x in range(0, 100, 100): 
         triangle2 = triangle(win, Point((x + a), (y + 40 + b)), Point((x + a), (y + 20 + b)), Point((x + 10 + a), (y + 40 + b)), colour)
         triangle3 = triangle(win, Point((x + 90 + a), (y + 40 + b)), Point((x + a + 100), (y + 20 + b)), Point((x + 100 + a), (y + 40 + b)), colour)

   for y in range(20, 80, 40):
      for x in range(10, 90, 20):
         triangle4 = triangle(win, Point((x + a), (y + 20 + b)), Point((x + 10 + a), (y + b)), Point((x + 20 + a), (y + 20 + b)), colour)


def patchBackgroundColours():
   for y in range(0, patchSize, 100):
      for x in range(0, patchSize, 100):
         tl = Point(x, y)
         br = Point(tl.x + 100, tl.y + 100)

         patchColouring(x, y, patchSize)
         rectangle(win, tl, br, colour)

      for x in range(0, patchSize, 200):
         
         patchColouring(x, y, patchSize)
         rectangle(win, Point(x, y), Point(x + 100, y + 100), "white")
         patchF(win, x, y, colour)
         
   for y in range(100, (patchSize-100), 100):
      for x in range(100, patchSize, 200):

         patchColouring(x, y, patchSize)
         rectangle(win, Point(x, y), Point(x + 100, y + 100), "white")
         patchP(win, x, y, colour)

patchBackgroundColours()
