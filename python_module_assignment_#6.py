#Write a Python program to configure the rounding to round up and round down a given decimal value. Use decimal.Decimal?
import decimal
print("Rounding to round up:")
decimal.getcontext().prec = 1
decimal.getcontext().rounding = decimal.ROUND_UP
print(decimal.Decimal(30) / decimal.Decimal(4))
print(f"Rounding to round down:")
decimal.getcontext().prec = 3
decimal.getcontext().rounding = decimal.ROUND_DOWN
print(decimal.Decimal(30) / decimal.Decimal(4))
print(f"Rounding to round up:")
print(decimal.Decimal('8.325').quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_UP))
print(f"Rounding to round down:")
print(decimal.Decimal('8.325').quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_DOWN))