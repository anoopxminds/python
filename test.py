import sys
import math

# Print system version

print("hello world");
print(sys.version);

x = 5;
y = "String";

print(type(x));
print(type(y));

x = "Test function";

# Test funtion 

def myfun():
    x = "new function";
print("python with " + x);

print(myfun())


#Global variable

def fun():
    print("Print inside function with :", s);

s = "test data";
fun();
print("Print outside with : ", s);    

#Multi line statement

s = "Multi "\
"line "\
"statement";

print(s);


print("A"*6);

x = 10;
y = 12;

string = "This value of x is {} and y is {}";


print(string.format(x, y))

from math import pi

print(pi);

# optional_params

list = {"Bread": 1, "Milk": 2, "Cake": 3, "Chocolate": 4, "butter": 5}
def show_list():
    for item_name,quantity in list.items:
        print(f"{quantity} x {item_name}");

show_list();





















