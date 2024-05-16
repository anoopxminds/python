#Handling exception with try and except
#using else and finally along with try and except
#raise an exception
#creating custom exception

print("================================= Method 1 ===================================")

def divide(a, b):
    try:
        res = a//b
        print(f"Result : {res}")
        
    except ZeroDivisionError:
        print(f"You are trying to dividing by zero !")
        
divide(2,0)

print("================================= Method 2 ===================================")

def divide1(a, b):
    try:
        res = a//b
        print(f"Result : {res}")
        
    except Exception as e:
        print(f"Error : {e}")
        
divide1(2,0)

print("================================= Method 3 ===================================")

def divide2(a, b):
    try:
        res = a//b
        print(f"Result : {res}")
        
    except Exception as e:
        print(f"Error : {e}")
        
    finally:
        print("Always exceuting !")
        
divide2(2,0)

print("================================= Method 4 ===================================")

class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f"{self.message}"
        
        
def divide_numbers(a, b):
    if b == 0:
        raise CustomError("Division by zero is not allowed.")
    return a / b
        
def divide3():
    try:
        result = divide_numbers(10, 0)
        print(f"Result : {result}")
    except CustomError as e: 
        print(f"Error : {e}")
            
divide3()   