#Removal all characters from a string except integers

string = "Total 10 and sub total 5 and 5"

res = "".join([i for i in string if i.isdigit()])

print(res);



