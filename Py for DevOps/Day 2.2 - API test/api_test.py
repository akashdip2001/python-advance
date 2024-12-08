# # As a DevOps Engineer, Your Developer has an API (Application Programming Interface) that you need to test.

# import requests
# # pip install requests ## install in my Global Python Environment in PC

# demo_url = "https://jsonplaceholder.typicode.com/posts"

# response = requests.get(url=demo_url)
# print(response)
# #output: <Response [200]> ## 200 means the request was successful

# # print(response.json()) # get list of dictionaries [{}, {}, {}]
# # print(type(response.json())) # <class 'list'>

# print(response.json()[0]) # get first dictionary {}



import requests

def test_api():
    demo_url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url=demo_url)
    print(response)
    return response.json()[0]

X = test_api() # call the function to test the API
print(X)