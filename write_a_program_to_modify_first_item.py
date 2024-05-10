#1. Write a program to modify first item of list in the following tuple

tuple_list_item = (11, [22, 33], 44, 55)

print(type(tuple_list_item))

tuple_list_item[1][0] = 10

print(tuple_list_item)


#2. Convert the following tuple to a string

tuple_list = ('p','y','t','h','o','n')

print(type(tuple_list))

string_from_tuple = "".join(tuple_list)

print(type(string_from_tuple))


print(string_from_tuple)

#3.Convert a string to list of tuples.
#Input: "Python is the popular programming language."
#Output:[(‘Python’, ‘is’), (‘the’, ‘popular’), (‘programming’, ‘language’)]

input_string ="Python is the popular programming language."
splitted_string = iter(input_string.split())
new_list = [(ele, next(splitted_string)) for ele in splitted_string]

print(new_list)

print("=========== Defferent way =============")

input_string1 ="Python is the popular programming language."

splitted_string1 = input_string1.split()

res = []

for i, word in enumerate(splitted_string1):
    if i % 2 == 0:
        res.append((word, splitted_string1[i+1]))

#printing result 

print("List after String to tuple conversion : " + str(res))
