#Iterate both lists simultaneously use zip method.

list1 = [10, 20, 30, 40]
list2 = [50, 60, 70, 80]

new_list = zip(list1, list2)

print(list(new_list));

for item1, item2 in zip(list1, list2):
    print(item1, item2)