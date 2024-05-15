#Write a Python program to generate a random color hex, a random alphabetical string, random value between two integers (inclusive) and a random multiple of 7 between 0 and 70. Use random.randint()  

import random

color = random.randrange(0, 2**24)
hex_color = hex(color)
std_color = "#" + hex_color[2::]

print(std_color)


#Write a Python program to generate a random alphabetical string

import string
import random

number_of_charactor = 10

random_string = "".join(random.choices(string.ascii_uppercase + string.digits, k = number_of_charactor))

print(f"Random generated string is : {str(random_string)}")

#Write a Python program to a random value between two integers (inclusive) and a random multiple of 7 between 0 and 70. Use random.randint()  

print(random.randint(0, 10))
print(f"random multiple of 7 between 0 and 70 : {random.randint(0, 10) * 7} ")

