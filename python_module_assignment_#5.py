#Write a Python program to construct a Decimal from a float and a Decimal from a string. Also represent the Decimal value as a tuple. Use decimal.Decimal

import decimal

pi_val = decimal.Decimal(3.14159)

print(pi_val)

print(f"pi value as a tuple : {pi_val.as_tuple()}")

num_str = decimal.Decimal("123.25")
print(f"type : {type(num_str)} : {num_str}")
print(num_str.as_tuple())