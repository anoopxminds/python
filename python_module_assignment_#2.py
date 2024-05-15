#Write a Python program to select a random element from a list, set, dictionary (value) and a file from a directory. Use random.choice()?

import random
import os

elements = [10,20,30,40,50]
print(f"Select random number from the given list : {random.choice(elements)}")
print(f"Select random number from the given list : {random.choice(elements)}")
print(f"Select random number from the given list : {random.choice(elements)}")

elements1 = set([10,20,30,40,50])

print(f"Select random number from the given set : {random.choice(tuple(elements1))}")
print(f"Select random number from the given set : {random.choice(tuple(elements1))}")
print(f"Select random number from the given set : {random.choice(tuple(elements1))}")


dict_list = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}

dict_key = random.choice(list(dict_list))
print(f" random value from a dictionary : {dict_list[dict_key]} ")
print(f" random value from a dictionary : {dict_list[dict_key]} ")
print(f" random value from a dictionary : {dict_list[dict_key]} ")
