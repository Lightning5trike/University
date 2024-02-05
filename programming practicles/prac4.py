
from graphics import *
import math


#question 1
def personalGreeting():
    name = input("name: ")
    capitalise = name.capitalize()
    print("Hello " + capitalise + ", nice to see you!")


#question 2
def formalName():
    fName = input("First name: ")
    lName = input("Last name: ")
    fLetter = fName[0]
    capsF = fLetter.upper()
    capsL = lName.capitalize()
    print(capsF + ". " +capsL)


#question 3
def kilos2pounds():
    kilos = float(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print("{0:0.2f} kilos is equal to {1:0.2f} pounds".format(kilos, pounds))


#question 4
def generateEmail():
    fName = input("First name: ")
    lName = input("Last name: ")
    yearLong = input("Year Started: ")
    fLetter = fName[0]
    year = yearLong[-2:]
    print(lName + "." + fLetter + "." + year + "@myport.ac.uk")


#question 5
def gradeTest():
    mark = int(input("mark: "))
#come back to

#question 6
def graphicLetters():
    word = input("word: ")
    win = GraphWin("graphicLetters")
    for letter in range(0, len(word)):
        x = word[letter]
        p = win.getMouse()
        y = Text(p, x)
        y.draw(win)


#question 7
def singASong():
    word = input("word: ")
    repeats = int(input("how many times repeated per line: "))
    lines = int(input("lines: "))
    for x in range(lines):
        for i in range(repeats):
            print(word + " ", end = '')
        print("\n")

#question 8
def exchangeTable():
    for i in range(0, 20):
        pounds = i*1.17
        print(i,"€" , " \t ", "£ {0:0.2f}".format(pounds))

#question 9
def makeInitialism():
    phrase = input("phrase: ")
    splitPhrase = phrase.split(' ')
    for word in splitPhrase:
        firstLetter = word[0]
        FLUpper = firstLetter.upper()
        print(FLUpper, end = " ")


#question 10
def nameToNumber():
    name = input("name: ")
    count = 0
    for letter in range(0, len(name)):
        x = name[letter]
        asciiLetter = ord(x) - 96
        count += asciiLetter
    print(count)

#question 11
def fileInCaps():
    fileText = input("What do you want written in the file: ")
    fileToOpen = open("fileInCaps.txt", "w")
    fileToOpen.write(fileText.upper())
    fileToOpen.close()
    fileToOpen = open("fileInCaps.txt", "r")
    print(fileToOpen.read())
    fileToOpen.close()

#question 12
def rainfallChart():
    fileToOpen = open("rainfall.txt", "r")
    count = 1
    for line in fileToOpen:
        split = line.split(' ')
        print(split[0])
        numberStr = split[1]
        number = int(numberStr[:len(numberStr)-1])
        print('*' * number)
    fileToOpen.close()
    
#question 13
def rainfallChart():
    rainfallFile = open("rainfall.txt", "r")
    InchesFile = open("Inches.txt", "w")
    for line in rainfallFile:
        split = line.split(' ')
        InchesFile.write(split[0] + " ")
        number = int(split[1])
        inches = number / 2.54
        formattedInches = "{0:0.2f}".format(inches)
        inchesString = str(formattedInches)
        InchesFile.write(inchesString + "\n")
    rainfallFile.close()
    InchesFile.close()

# #question 14
def wc():
    fName = input("file name: ")
    lines = 0
    characters = 0
    words = 0
    openFileName = open(fName+".txt", "w")
    # fileText = input("What do you want written in the file: ")
    # openFileName.write(fileText)
    openFileName.close()
    openFileName = open(fName+".txt", "r")
    for line in openFileName:
        lines += 1
        row = line[:-1].split()
    for word in row:
        word += 1
        characters += len(word)
    print(words)
    print(characters)
    print(lines)


wc()

