# interest.py - an example use of functions


def calcFutureValue(amount, years):
    interestRate = 0.035
    for year in range(years):
        amount = amount * (1 + interestRate)
    return amount


def futureValue():
    amount = float(input("Enter an amount to invest: "))
    years = int(input("Enter the number of years: "))
    finalValue = calcFutureValue(amount, years)
    print("Investing GBP {0:0.2f} for {1} years".format(amount, years),
          "will result in GBP {0:0.2f}.".format(finalValue))
