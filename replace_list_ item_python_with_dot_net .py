#Replace list’s item Python with .Net in the following list

languages = ['Java', 'Python', 'JavaScript']
print(languages)
to_replace = 'Python'
with_item = '.Net'

# convert list to string
test_string = " ".join(languages)

updated_list = test_string.replace(to_replace, with_item)

# convert updated string back to list
modified_list = updated_list.split()     

print(modified_list)