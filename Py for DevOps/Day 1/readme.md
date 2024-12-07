- Day 1
01) Introduction
02) Python Basics for DevOps
03) Control Flow & Functions

---

# Concepts

## Run .Py
```
>>> python .\hellow.py
```

## Comments
```
`#` Single line comment
```
```
"""
Multi line comments
"""
```

---

## Variables and constants

CONSTANT = 1, 2, 3

variable = a, name, age
a = 1
a = 2
a = 3

name = "Akashdip"
name = "Tushar"

So, name is a variable and value is a constant

---

## [Data Types](https://github.com/akashdip2001/ML-Machine-Learning/blob/main/py/README.md#data-types)

**Example of ✅ Variables with ➡️ Data-Types:**

```python
name = "Alice"  # String variable
age = 30        # Integer variable
height = 5.6    # Float variable
mathEq = 12+5j  # Complex
ans = True      # Bool
```
- ✅ Python auto detect the DataType.
- ✅ But for user input py always take String

Output
```python
print(type(name))
# Srting
print(type(age))
# int
print(type(height))
# float
```

---

## [Type Casting](https://github.com/akashdip2001/ML-Machine-Learning/blob/main/py/README.md#input-output)

### ✅ Ex 1

```python
a=1

print(a)
print(float(a))
```
output:
```go
1
1.0
```

### ✅ Ex 2

- **In python , always take input as a String.**
- 1st we take an input and store in a variable.

```python
# python always take user input as a String
variable = input("Enter number: ")
print(variable)
print(type(variable))

# Output
# Enter number: 12
# 12
# 'str' ---> String
```

```python
# But we Manually change it
variable = int(input("Enter number: "))
print(variable)
print(type(variable))

# Output
# Enter number: 12
# 12
# 'int'
```

---

## [Operators](https://github.com/akashdip2001/ML-Machine-Learning/blob/main/py/README.md#operators)

a = 100
b = 200

- Arithmetic Operators `+ - * /`
- Assignment Operators `=` , c = (a + b)
- Comparison Operators `< > <= >= ==` 
- Incrementing and Decrementing Operators
- Logical Operators `& | !` --> `and` `or` `not`

---

## Input

```python
city = input("Enter your city Name! ")

print("Your city name is :",city)
```
output
```bash
#Enter your city Name! Haldia
#Your city name is : Haldia
```

## String Formatting

```python
city = input("Enter your city Name! ")

print(f"Your city name is : {city}")
```
output
```bash
#Enter your city Name! Haldia
#Your city name is : Haldia
``` 

## Manipulate Strings

```python
name1 = input("Enter your name :")
name2 = input("Enter Your Frd. name :")

about = f"Hellow friends, this is {name1}"
print(about)

x = about.replace("friends",name2)
print(x)
```
output:
```bash
#Hellow friends, this is Akashdip
#Hellow XYZ, this is Akashdip
```

### Everything I do with this `function` with string

```python
print(dir(about))
```
output:
```
Enter your name :A
Enter Your Frd. name :B
Hellow friends, this is A
Hellow B, this is A
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

### This Way

```python
a = 5
print(dir(a))
```
and you get everything you do with this integer. ...

---
---

# Conditionals

### indentation <`4 block space`>

```python
a = 10
b = 30
c = 50

if a > b:
    print("A is bigger")
```

#### Ex: 1

```python
env = "dev"
# env = "prod"

if env == "dev":
    print("Yes this is")
else:
    print("No, it's not")
```

#### Ex: 2

```python
a = 10
b = 30
c = 50

if a > b and a > c:
    print("A is biggest among a, b, c")
elif b > a and b > c:
    print("B is biggest")
elif c > a and c > b:
    print("C is biggest")
else:
    print("All are equal")
```

---

## Create a function

```yaml
def: define a function
```

```python
def Check_biggest(a, b, c):
    
    if a > b and a > c:
        print("A is biggest among a, b, c")
    elif b > a and b > c:
        print("B is biggest")
    elif c > a and c > b:
        print("C is biggest")
    else:
        print("All are equal")



Check_biggest(10, 20, 30)
```
Now I have my own function with own logic.

---
---

# [core Data Structures](https://github.com/akashdip2001/ML-Machine-Learning/tree/main/py#list-tuple-set-dict)

### Data Structures is a subset of DSA.
### Data Structures --> How your data has organize.

- [List](https://github.com/akashdip2001/ML-Machine-Learning/tree/main/py#list) : collection pof data `[1, 2.5, True, "String", 2.5]`
- [Sets](https://github.com/akashdip2001/ML-Machine-Learning/tree/main/py#set)  : collection of uniq elements `{1, 2, 3}`
- [Dict](https://github.com/akashdip2001/ML-Machine-Learning/tree/main/py#dictionary)   : key with its value `{'age': 21}`
- [Tuple](https://github.com/akashdip2001/ML-Machine-Learning/tree/main/py#tuple)   : same as `List` but can't Remove or edit `(1, 2, 3)`
- [Array (not core in python)](https://github.com/akashdip2001/ML-Machine-Learning/tree/main/py#arrays) : only smiler Data types -> only int or only float...


# [Next : **Day 2**](../Day%202/readme.md)
