#Input a number check if the number is positive or negative or zero and display an appropriate message use nested if statement

n=int(input("Enter the number : "));

if n >= 0:
    if n == 0:
        print("This number is zero");
    else:
        print("This is a positive number");
else:
    print("This is a negative number");
