# Write a Python program to check if a given value is a method of a user-defined class. Use types.MethodType()

import types

class UserClass:
    def a():
        return 1
    
    def b():
        return 1
    
def c():
    return 2

print(isinstance(UserClass().a, types.MethodType))
print(isinstance(UserClass().b, types.MethodType))
print(isinstance(c, types.MethodType))
print(isinstance(max, types.MethodType))
print(isinstance(abs, types.MethodType))


    