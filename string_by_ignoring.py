#Find all occurrences of a substring in a given string by ignoring the case

str1 = "Find all occurrences of a substring in a given string by ignoring the case."

sub_string = "string";

temp = str1.lower();

count = temp.count(sub_string.lower());
print(str(count));