#program to create a function that takes a number as argument, and print whetehr the number is divisibl by 5 and 7

number = input("Enter a number to check Divisible by 5 and 7 : ");

number = int(number)
#print(type(number))

if (number) :
    if number % 5 == 0 and number % 7 == 0 :
        print("Number "+ str(number) + " is divisibl by 5 and 7")
    else:
        print("Number "+ str(number) + " is not divisibl by 5 and 7")

