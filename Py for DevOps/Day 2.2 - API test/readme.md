# [Pre : **Day 2 : Data Structures**](../Day%202%20-%20Data%20Structures/readme.md)

---

## As a DevOps Engineer, Your Developer has an API (Application Programming Interface) that you need to test.
```python
import requests
# pip install requests ## install in my Global Python Environment in PC
```
```python
demo_url = "https://jsonplaceholder.typicode.com/posts" # https://reqres.in/api/users

response = requests.get(url=demo_url)
print(response)
#output: <Response [200]> ## 200 means the request was successful
```

#### `print(response.json())` # get list of dictionaries [{}, {}, {}]
#### `print(type(response.json()))` # <class 'list'>
```python
print(response.json()[0]) # get first dictionary {}
```