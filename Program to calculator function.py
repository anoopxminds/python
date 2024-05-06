#Program to create a calculator function such that it can accept two numbers and calculate addition and subtraction,division,multiplication .All the result should be returned in a single return call.

#add two numbers
def add(x, y):
    return x + y;

#Substract two numbers
def substract(x,y):
    return x-y;

# Divide two numbers
def divide(x, y):
    return x/y;

# Multiply two numbers
def multiply(x, y):
    return x*y;
def show_list() :
    print("Select one operation to calculate : ");
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    user_input = input("Enter choice (1/2/3/4): ");
    print(type(user_input))
    while True:
        if user_input in ('1','2','3','4') :
            try:
                num1 = float(input("Enter first number : "));
                num2 = float(input("Enter second number : "));
            except ValueError:
                print("Invalid number please enter valid.");
                continue;
    
            print(user_input);

            if (user_input == '1') :
                print(num1, " + ", num2, " = ", add(num1, num2));
            elif (user_input == '2'):
                print(num1, " - ", num2, " = ", substract(num1, num2));
            elif (user_input == '3'):
                print(num1, " * ", num2, " = ", multiply(num1, num2));
            elif (user_input == '4'):
                print(num1, " / ", num2, " = ", divide(num1, num2));
        else :
            print("Invalid input");

def main() :
    show_list();


main();
