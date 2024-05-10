#1. Write a program to modify first item of list in the following tuple

tuple_list_item = (11, [22, 33], 44, 55)

print(type(tuple_list_item))

tuple_list_item[1][0] = 10

print(tuple_list_item)


#2. Convert the following tuple to a string

tuple_list = ('p','y','t','h','o','n')

print(type(tuple_list))

string_from_tuple = ','.join(tuple_list)

print(type(string_from_tuple))


print(string_from_tuple)

#3.Convert a string to list of tuples.
#Input: "Python is the popular programming language."
#Output:[(‘Python’, ‘is’), (‘the’, ‘popular’), (‘programming’, ‘language’)]

input_string ="Python is the popular programming language."
splitted_string = iter(input_string.split())
new_list = [(ele, next(splitted_string)) for ele in splitted_string]

print(new_list)



