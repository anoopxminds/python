#Assignment on Dictionary

languages = ['Python', 'Java', 'c#']
versions = [3, 22, 12]

list = dict(zip(languages, versions))

print("Dictionary list : ", list)


# Delete some keys from the following dictionary

empl_dict = {
    "name": "Karthik",
    "age": 25,
    "salary": 80000,
    "jobtitle": "Software developer"
}

print("Dictionary list : ", empl_dict)

#Remiving salary 

removed_key = "salary"

print("The removing key is : " + str(removed_key))

#Remiving key and value 

removed_value = empl_dict.pop(removed_key, "Key is not found!")

print("The removed key's value is : " + str(removed_value))

print("Dictionary after removed key : ", str(empl_dict))

# Rename the key jobtitle to position

empl_dict['position'] = empl_dict.pop('jobtitle')

print("Dictionary after change key : ", str(empl_dict))
