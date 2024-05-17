def custom_decorator(func):
   def wrapper(*args, **kwargs):
       return func(*args, **kwargs)
   return wrapper
       

@custom_decorator
def actual_function(a, b):
    return a+b

@custom_decorator
def doubled(number):
        return number*number
    

print(actual_function(1,2))
print(doubled(2))
        
    
