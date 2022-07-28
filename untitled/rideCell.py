import jsonpath
import requests
import json
import sys
from requests.auth import HTTPBasicAuth


def test1():
    url = "https://github.com/django/"
    # response = requests.get(url, auth=HTTPBasicAuth('name', 'pwd'))
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data

    json_data1 = response.json()
    return json_data1


def test2():
    response = requests.get("https://github.com/django")
    struct = {}
    try:
        try:  # try parsing to dict
            dataform = str(response).strip("'<>() ").replace('\'', '\"')
            struct = json.loads(dataform)
        except:
            print(repr(response))
            print(sys.exc_info())
    except:
        pass


def test3():
    response = requests.get("https://github.com/django")
    struct = {}
    try:
        response = response.decode('utf-8').replace('\0', '')
        struct = json.loads(response)
    except:
        print('bad json: ', response)
    return struct


def test4():
    url = "https://api.github.com/users/django/repos"
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data


# test4()
# # test3()

url = "https://api.github.com/users/django/repos"
response = requests.get(url)
# json_data = json.loads(response.text)
print(response.text)
# jp = jsonpath.jsonpath(response.json(), "$.*['name']")
# jp1 = jsonpath.jsonpath(response.json(), "$.*['description']")
jp = jsonpath.jsonpath(response.json(), "$.*.name")
jp1 = jsonpath.jsonpath(response.json(), "$.*.description")

# print(jp)
# print(jp1)

# dict = {}
# for key in jp:
#     for value in jp1:
#         dict[key] = value
#         jp1.remove(value)
#         break
#
# print(dict)


dict1 = {'k1': 'v1', 'k2': 'v2'}
dict2 = {'k2': 'v2', 'k1': 'v1'}

# if dict1 == dict2:
# print("good")
