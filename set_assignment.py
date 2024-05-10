#set assignment
# Write a program to return a set of elements present in set1 or set2, but not both

q1_set1 = {10,30,100,150,20}
q1_set2 = {30,40,110,20,150}

#Removing common elements on set 1 and set2

q1_set3 = q1_set1.symmetric_difference(q1_set2)

print(f"new set after removed common elements {q1_set3}") # {100, 40, 10, 110}

# New set with common elements from set1 and set2
q1_set4 = q1_set1.intersection(q1_set2)

print(f"common elements {q1_set4}") #{20, 150, 30}


#2) Write a Python program to return a new set with unique items from both sets by removing duplicates.


q2_set1 = {10,30,100,150,20}
q2_set2 = {30,40,110,20,150}

q2_set3 = q2_set1.union(q2_set2)

print(f"common elements {q2_set3}") # result : {100, 40, 10, 110, 20, 150, 30}