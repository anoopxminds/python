#Python program to create a decorator that logs the function name,arguments and return value of a function

def decorator(func):
    def wrapper(*args, **kwargs):
        
        print(f"function name : {func.__name__} with args : {args} and kwargs : {kwargs}")
        
        res = func(*args, **kwargs)
        
        print(f"Function name : {func.__name__} and returning : {res}")
        
        return res
    return wrapper


@decorator
def multiply_value(a, b):
    return a * b


result = multiply_value(2, 4)
print(f"Result of multiply two values : {result}")

