#Write a Python program to return a new set with unique items from both sets by removing duplicates.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

unique_items = set1.symmetric_difference(set2)

print(unique_items)