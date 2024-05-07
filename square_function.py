#Create an outer function which will accept 2 numbers as arguments.Create an inner function which will return the square of number.

def outer_fun(num1, num2):

    def inner_fun(num1, num2):
        return num1**num2;

    return inner_fun(num1, num2);


print(str(outer_fun(5, 2)));

