#Inheritance Assignment

#1.Create a class person having instance variables name,age,height and weight And method display to print the variable values. 
# Create a sub class Student which will inherit all the variables and method of Person.
print("================== #1 ===============================")

class Person:
    
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
        
    def display_details(self):
        print(f"Person Name : {self.name}")
        print(f"Person Age : {self.age}")
        print(f"Person height : {self.height}")
        print(f"Person weight : {self.weight}")
        
class Student(Person):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight)
        
        
        
person = Person("Person 1", "20 Years", "5 feet", "70 kg")

person.display_details()

student = Student("Person 2", "10 Years", "5 feet", "50 kg")

student.display_details()

#2.Create a parent class Account with instance variables name and balance. 
# Create sub class SavingsAccount with instance variable interestRate.Define methods withDraw(),deposit() and getBalance() in parent class.define interestAmount method in child class.
print("================== #2 ===============================")

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)
        
    def withDraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount :
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
            
    def getBalance(self):
        print("\n Net Available balance =", self.balance)
        
        
class SavingsAccount(Account):
        time_period = 5
        rate_of_interest = 8
        def __init__(self, name, balance):
             super().__init__(name, balance)
        
        def interestAmount(self):
            amount = (self.balance * self.time_period * self.rate_of_interest)/100
            self.balance += amount
            print("\n Net Interest =", amount)
            
            
account = Account("Anoop", 1000)
account.getBalance()
account.withDraw()
account.getBalance()
account.deposit()
account.getBalance()

savingsAccount = SavingsAccount(account.name, account.balance);
savingsAccount.interestAmount()

            
             
        
    
            