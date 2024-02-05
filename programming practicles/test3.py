class bankaccount:
    def __init__(self):
        self.balance = 100
        
    
    def getBalance(self):
        return self.balance

    def processTransaction(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("You are no longer in credit. Please see the bank manager")


def testBankAccount():
    b = bankaccount()
    b.processTransaction(70)
    print(b.getBalance())
    b.processTransaction(40)
    print(b.getBalance())
    

#testBankAccount()



class bankaccount2:
    def __init__(self):
        self.balance = 100
        self.overdraftUsed = False
        
        
    
    def getBalance(self):
        return self.balance
    

    def arrangeOverdraft(self):
        self.overdraftUsed = True
        if self.balance < -50:
            print("you have no money in your overdraft go see a bank manager")


    def processTransaction(self, amount):
        if -50 < self.balance < 0:
            print("You are going into ovedraft")
            self.balance -= amount
        elif self.balance < -50:
            print("payment not authorised")
            overdraftUsed = True
        else:
            overdraftUsed = False
            self.balance -= amount


    

def testBankAccount2():
    b2 = bankaccount2()
    b2.arrangeOverdraft()
    b2.processTransaction(40)
    print(b2.getBalance())
    
testBankAccount2()
