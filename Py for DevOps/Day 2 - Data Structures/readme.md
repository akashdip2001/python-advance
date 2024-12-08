# [Pre : **Day 1**](../Day%201/readme.md)

---

- Day 2

05) [ ] Networking & API Interactions
06) [x] Core Date Structures (DSA)
07) [ ] OOP
08) [ ] Infrastructure as Code

---


# [core Data Structures](https://github.com/akashdip2001/ML-Machine-Learning/tree/main/py#list-tuple-set-dict)

### Data Structures is a subset of DSA.
### Data Structures --> How your data has organize.

- [List](https://github.com/akashdip2001/ML-Machine-Learning/tree/main/py#list) : collection pof data `[1, 2.5, True, "String", 2.5]`
- [Sets](https://github.com/akashdip2001/ML-Machine-Learning/tree/main/py#set)  : collection of uniq elements `{1, 2, 3}`
- [Dict](https://github.com/akashdip2001/ML-Machine-Learning/tree/main/py#dictionary)   : key with its value `{'age': 21}`
- [Tuple](https://github.com/akashdip2001/ML-Machine-Learning/tree/main/py#tuple)   : same as `List` but can't Remove or edit `(1, 2, 3)`
- [Array (not core in python)](https://github.com/akashdip2001/ML-Machine-Learning/tree/main/py#arrays) : only smiler Data types -> only int or only float...

---

## Data Structures

## ☀️ List
```python
## List

envirorment = ["dev", "prd", "stg", "test"]
# print(dir(envirorment))

print(len(envirorment))
# output: 4 (0, 1, 2, 3)

envirorment.append("bastion")
print(envirorment)

# You dont know What is append ??
print(envirorment.append.__doc__) # docomentation
# output: Append object to the end of the list.
```

```bash
$: python
>>> import keyword
>>> keyword.kwlist 
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>>
>>> len(keyword.kwlist)
35
>>>
>>> exit()
$:
```

---

## ☀️ Dictionary

```python
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
```

output:
```bash
$: Akashdip
$: {'name': 'Akashdip', 'age': 21, 'city': 'Kolkata', 'country': 'India', 'is_student': True, 'envirorment': ['dev', 'prd', 'stg', 'test', 'bastion']}
```

---

## ☀️ Sets
```python
data = {}
print(type(data))
# output: <class 'dict'>
```
```python
data = {1}
print(type(data))
# output: <class 'set'>
```
### Remove duplicates
```python
device_id = {1, 2, 3, 3, 4, 5, 5} # Total 7 elements
print(len(device_id)) # But output: 5
## Remove duplicates
```
```python
new_id = {6, 7, 8, 9, 10, 10, 1}
print(device_id.union(new_id)) # output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(device_id.intersection(new_id)) # output: {1}
```

---

## ☀️ Tuples

#### Tuples are immutable, ordered collections of elements. They are similar to lists, but they cannot be changed after they are created. Tuples are defined using parentheses () and elements are separated by commas.
```python
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(type(days_of_week)) # output: <class 'tuple'>
print(days_of_week[0]) # output: Monday
```

---

## ⚠️ array

### not core Data Structure in python, array is a module in python
##### array is a list of elements of the same type, array is faster than list, array is used when we need to store large number of elements of the same type
```python
import array

arr = array.array('i', [1, 2, 3, 4, 5])
print(arr)
print(arr[0])
print(arr[1])
print(arr[2])
```

---

# [Next : **API Test**](../Day%202.2%20-%20API%20test/readme.md)
# [Next-Next : **docker-using-python**](../Day%202.3%20-%20OOPs/readme.md)
