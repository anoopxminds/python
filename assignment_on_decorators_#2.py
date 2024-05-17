#Program to create a decorator to convert the return value of a function to a specified data type.

def convert_to_data_type(data_type):
    def decoration(func):
        def wrapper(*args, **kwargs):
            result =  func(*args, **kwargs)
            return data_type(result)
        return wrapper
    return decoration

@convert_to_data_type(int)
def add_numbers(a, b):
    return a + b
    
result = add_numbers(2, 4)

print(f"Result is {result} and data type is {type(result)}")

@convert_to_data_type(str)
def concatenate_string(a, b):
    return a + b


result = concatenate_string("Python", " Decorator")

print(f"Result is {result} and data type is {type(result)}")

