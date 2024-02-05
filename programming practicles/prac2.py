from cmath import pi
import math

#question1
def circumferenceOfCircle():
    rad = float(input("input value of radius: "))
    circ = rad * 2 * pi
    print("circumference: ", circ)


#question 2
def areaOfCircle():
    rad = float(input("input value of radius: "))
    area = (rad^2) * pi
    print("area: ", area)

#question 3
def costOfPizza():
    dia = float(input("diameter: "))
    area = ((dia/2)^2) * pi
    price = 1.5 * area
    print("price: ", price)

#question 4
def SlopeOfLine():
    x1 = float(input("x1: "))
    x2 = float(input("x2: "))
    y1 = float(input("y1: "))
    y2 = float(input("y2: "))
    grad = (y2-y1)/(x2-x1)
    print("gradient: ", grad)

#question 5
def distanceBetweenPoints():
    x1 = float(input("x1: "))
    x2 = float(input("x2: "))
    y1 = float(input("y1: "))
    y2 = float(input("y2: "))
    squared = ((x2-x1)^2) + ((y2-y1)^2)
    dist = math.sqrt(squared)
    print("distance: ", dist)

#question 6
def travelStatistics():
    speed = float(input("speed: "))
    time = float(input("time: "))
    dist = speed * time
    fuel = dist / 5
    print("fuel: ", fuel)    

#question 7
def sumOfSquares():
    num = int(input("Input number of repetitions: "))
    sum = 0
    for i in range(num):
        sum+= i^2
    print(sum)
sumOfSquares()
#come back to this



#question 8
def averageOfNumbers():
    amount = input("how many numbers are in the list: ")
    total = 0
    for i in range(amount):
        num = input("enter a number: ")
        total+=amount
    print(total/num)

#question 9
def fibonacci():
    n = int(input("input a number: "))
    num1 = 1
    num2  = 1
    count = 0
    while count < (n-2):
        newNum = num1 + num2
        num1 = num2
        num2 = newNum
        count+=1
    print(newNum)

