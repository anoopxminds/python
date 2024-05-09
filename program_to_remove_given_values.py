#Write a program to remove 10,20,30 from set1 = {10, 20, 30, 40, 50}

set1 = {10, 20, 30, 40, 50}

print(f"Before remove : {set1}")

to_remove = 10,20,30

set1.difference_update(to_remove)


print(f"After removed : {set1}")

