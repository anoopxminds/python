#Program to create a calculator function such that it can accept two numbers and calculate addition and subtraction,division,multiplication .All the result should be returned in a single return call.

def show_list() :
    list = [];
    while True:
            try:
                num1 = float(input("Enter first number : "));
                num2 = float(input("Enter second number : "));
            except ValueError:
                print("Invalid number please enter valid.");
                continue;
            list.append(num1 + num2)    
            list.append(num1-num2)  
            list.append(num1*num2)  
            list.append(num1/num2)  
            string = ', '.join(map(str,list));
            print(string);
    
show_list();