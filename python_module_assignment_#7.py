#Write a Python program to create a shallow copy of a given list. Use copy.copy8. 
import copy
nums_x = [1, [2, 3, 4]]
nums_y = copy.copy(nums_x)
print(f"Copy of the said list: {nums_y}")
nums_x[1][1] = 10
print(f"Change the value of an element of the original list: {nums_x}")
print(f"Second list: {nums_y}")
nums =  [[1], [2]]
nums_copy = copy.copy(nums)
print(f"Original list: {nums}")
print(f"Copy of the said list: {nums_copy}")
nums[0][0] = 0
print(f"Change the value of an element of the original list: {nums}")
print(f"Second list: {nums_copy}")