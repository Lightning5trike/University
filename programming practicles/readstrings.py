# readstrings.py - A demonstration of while loops to validate user input


# (note the need for string == "" to appear twice).
def getString1():
    string = ""
    while string == "":
        string = input("Enter a non-empty string: ")
        if string == "":
            print("You didn't enter anything!")
    return string


# The same validation example, this time using the
# loop-and-a-half pattern.
def getString2():
    while True:
        string = input("Enter a non-empty string: ")
        if string != "":
            break
        print("You didn't enter anything!")
    return string
