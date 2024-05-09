#Write a program to return a set of elements present in set1 or set2, but not both

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

new_set = set1.symmetric_difference(set2)

print(f"After update {new_set}")