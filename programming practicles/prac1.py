# Practical Worksheet P1: Getting started with Python
# Elia Fetta, up2109012


def sayHello():
    print("Hello world")


def count():
    for i in range(10):
        print(i)


def double():
    # here we use the built-in function int since we expect a whole number
    number = int(input("Enter a whole number: "))
    doubled = 2 * number
    print("If you double", number, "you get", doubled)


def kilos2pounds():
    # here we use float since a non-whole number is an acceptable input
    kilos = float(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print("The weight in pounds is", pounds)



#worksheet start

#question 1
def sayName():
    name = input("Enter your name: ")
    print(name)

#question 2
def sayHello2():
    print("Hello")
    print("World")

#question 3
def euros2pounds():
    euronum = float(input("How many euros would you like to convert: "))
    pounds = euronum * 1.17
    print("£", pounds)

#question 4
def sumDifference():
    num1 = float(input("enter your first number: "))
    num2 = float(input("enter your second number: "))
    sum = num1+num2
    print("the sum is: ", sum)
    if num1 >= num2:
        difference = num1 - num2
    else:
        difference = num2 - num1
    print("the difference between these numbers is: ", difference)

#question 5
def changeCounter():
    onep = float(input("How many 1p coins: "))
    twop = float(input("How many 2p coins: "))   
    fivep = float(input("How many 5p coins: ")) 
    TotTwop = twop * 2
    TotFivep = fivep * 5
    total = onep + TotTwop + TotFivep
    print("you have: ", total, "pence")

#question 6
def tenHellos():
    for i in range(10):
        print("hello, world")

#question 7
def countTo():
    num = int(input("Enter a whole number to count up to: "))
    for i in range(1, num+1):
        print(i)

#question 8
def zoomZoom():
    num = int(input("Enter a whole number of zooms: "))
    for i in range(1, num+1):
        print("zoom ", i)    

#question 9
def weightsTable():
    for i in range(1, 101):
        print(i, " \t ", i*2.205)

#question 10
def futureValue():
    intPrice = float(input("what was the initial price: "))
    years = float(input("how many years: "))
    count = 0
    while count < years:
        investment  = intPrice * 0.035
        intPrice += investment
        count = count + 1
    print(intPrice)


