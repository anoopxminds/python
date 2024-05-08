#Given a nested list ['a', ['bb', 'cc'], 'd']Insert item ‘dd’ to the second sublist’s first position so that resulting list will be['a', [‘dd’,'bb', 'cc'], 'd']

nested_list = ['a', ['bb', 'cc'], 'd']

print(nested_list)

new_item = 'dd'

nested_list[1].insert(0, new_item)

print(nested_list)