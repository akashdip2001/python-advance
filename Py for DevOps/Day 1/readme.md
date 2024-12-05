# Comments
```
`#` Single line comment
```
```
"""
Multi line comments
"""
```

---

# Variables and constants

CONSTANT = 1, 2, 3

variable = a, name, age
a = 1
a = 2
a = 3

name = "Akashdip"
name = "Tushar"

So, name is a variable and value is a constant

---

# [Data Types](https://github.com/akashdip2001/ML-Machine-Learning/blob/main/py/README.md#data-types)

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

# [Type Casting](https://github.com/akashdip2001/ML-Machine-Learning/blob/main/py/README.md#input-output)

## ✅ Ex 1

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

## ✅ Ex 2

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

# [Operators](https://github.com/akashdip2001/ML-Machine-Learning/blob/main/py/README.md#operators)

a = 100
b = 200

- Arithmetic Operators `+ - * /`
- Assignment Operators `=` , c = (a + b)
- Comparison Operators `< > <= >= ==` 
- Incrementing and Decrementing Operators
- Logical Operators `& | !` --> `and` `or` `not`

---

# Input

```python
city = input("Enter your city Name! ")

print("Your city name is :",city)
```
output
```bash
Enter your city Name! Haldia
Your city name is : Haldia
```

# String Formatting

```python
city = input("Enter your city Name! ")

print(f"Your city name is : {city}")
```
output
```bash
Enter your city Name! Haldia
Your city name is : Haldia
```




