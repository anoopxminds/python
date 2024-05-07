#Accept 3 input strings compare it and print in alphabetic order
from itertools import accumulate

str_list = []
for i in range(3):
    new_string = input("Enter string :")
    print("String added : ", new_string)
    str_list.append(new_string)
    str_list.sort();
    print(str_list)


    
