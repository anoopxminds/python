#Remove all empty string from a given list of strings

#Removing empty string using if

string_list = ["Python", "Java", "", "PHP", ""]

refined_list = [];
for i in string_list:
    if (i != ""):
        refined_list.append(i);
print(refined_list);

#Removing empty string using filter

new_list = list(filter(None, string_list));

print(new_list);
