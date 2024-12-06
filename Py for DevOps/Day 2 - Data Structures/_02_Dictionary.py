# Import envirorment from 01 List.py
from _01_List import envirorment

## Dictionary

data = {
    "name" : "Akashdip",
    "age" : 21,
    "city" : "Kolkata",
    "country" : "India",
    "is_student" : True
}

# print(data)
print(data["name"])

# data.update({"name" : "Akash"})
data.update({"envirorment": envirorment})
print(data)