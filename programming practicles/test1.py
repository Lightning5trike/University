import math 
def pizzaEating():
    tRadius = float(input("Total pizza radius (cm): "))
    calMonthly = int(input("How many calories of pizza do you want to eat per month: "))
    toppingRadius = tRadius - 4
    #math couldnt be imported hence why no squaring
    toppingArea = math.pi * (toppingRadius **2 ) #would be pi * toppingRadius^2
    baseArea = (math.pi * (tRadius * tRadius)) - toppingArea
    totalCal = (2.7 * toppingArea) + (0.9 * baseArea)
    pizzaMonthly = calMonthly//totalCal
    print("The radius of the topping region is: ", toppingRadius, "cm")
    print("The area of the topping region is: ", toppingArea, "cm^2")
    print("The number of calories in the pizza is: ", totalCal)
    print("The maximum number of complete pizzas of this size we should eat in a month is: ", pizzaMonthly)

pizzaEating()