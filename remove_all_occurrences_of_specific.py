#Remove all occurrences of a specific item from a list.

my_list = [1, 10, 20, 10, 21, 16, 18, 10, 22, 10, 8, 10]

print(my_list)

remove_item = 10

element_count = my_list.count(remove_item)

for i in range(element_count) :
    my_list.remove(remove_item)

print(my_list)

#Remove all occurrences of a specific item from a list of string.

list_of_string = ['Python', 'Java', 'Python', 'Javascript', 'Python', 'PHP']

print(list_of_string)

remove_string = 'Python'

to_rm_str_count = list_of_string.count(remove_string)

for s in range(to_rm_str_count):
    list_of_string.remove(remove_string)

print(list_of_string)







    

