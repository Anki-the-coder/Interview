import requests
import json
import jsonpath

# get
# get_baseURL = "https://reqres.in/api/users?page=2"
# get_BaseAPI = requests.get(get_baseURL)
# print(get_BaseAPI.content)
# assert get_BaseAPI.status_code == 200


# delete
# delete_baseURL = "https://reqres.in/api/users/2"
# delete_baseAPI = requests.delete(delete_baseURL)
# print(delete_baseAPI.text)
# assert delete_baseAPI.status_code == 204


# post
post_baseURL = "https://reqres.in/api/users"
poojaFile = open("C:\\Auto\\API\\poojapost.json", "r")
poojaFile_Json = json.loads(poojaFile.read())
post_baseAPI = requests.post(post_baseURL, poojaFile_Json)
print(post_baseAPI.content)
assert post_baseAPI.status_code == 201


# put
# put_baseURL = "https://reqres.in/api/users/2"
# put_file = open("C:\\Auto\\API\\poojapost.json","r")
# putfile_json = json.loads(put_file.read())
# put_baseAPI = requests.put(put_baseURL,putfile_json)
# print(put_baseAPI.content)
# assert put_baseAPI.status_code == 200
# jp = jsonpath.jsonpath(put_baseAPI, 'name')


# get_baseURL = "https://github.com/django"
# get_BaseAPI = requests.get(get_baseURL)
# # print(get_BaseAPI.text)
# json_data = json.loads(get_BaseAPI.text)
# print(json_data)
# print(get_BaseAPI.content)
# print(get_BaseAPI.text)
