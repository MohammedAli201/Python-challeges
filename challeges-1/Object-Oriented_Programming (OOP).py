
""" OOP helps us to organize the code  using objects and classes: This example will
take real-world scenrio. is Banking app represents customers as objects with attributes like name and balance
 """

class Customer: 
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
            self.balance += amount
            return f"New balance : ${self.balance}"
    
    def withdraw(self,amount):
         self.balance -=amount
         return f"withdraw money then the balanced is :${self.balance}"
     
def customerInput():       
    customerNmae = input("Customer name")
    try:
        amount = int(input("Amount :  "))
        customer1 = Customer(customerNmae, amount)

        deposite = int(input("amount to deposite : "))
        print(customer1.deposit(deposite))
    except ValueError:
        print("Invalid input! Please enter a number.")
        

customerInput()

