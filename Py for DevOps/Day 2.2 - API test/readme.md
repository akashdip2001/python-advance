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

#### `print(response.json())` get list of dictionaries [{}, {}, {}]
#### `print(type(response.json()))` <class 'list'>

```python
print(response.json()[0]) # get first dictionary {}
```

# Rap all in a function

```python
import requests

def test_api():
    demo_url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url=demo_url)
    print(response)
    return response.json()[0]

X = test_api() # call the function to test the API
print(X)
```
Output:
```bash
PS C:\Users\akash\Desktop\Py Projects\python-advance\Py for DevOps\Day 2.2 - API test> python .\api_test.py
<Response [200]>
{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
PS C:\Users\akash\Desktop\Py Projects\python-advance\Py for DevOps\Day 2.2 - API test> 
```