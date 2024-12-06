# sets

data = {1}
print(type(data))
# output: <class 'dict'> --> data = {}
# output: <class 'set'> --> data = {1}

device_id = {1, 2, 3, 3, 4, 5, 5} # Total 7 elements
print(len(device_id)) # But output: 5
## Remove duplicates

new_id = {6, 7, 8, 9, 10, 10, 1}
print(device_id.union(new_id)) # output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(device_id.intersection(new_id)) # output: {1}