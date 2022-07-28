import requests
import json
import jsonpath

print("1233333")
# def test_postAPI():
#     global Id
#     post_url = "https://reqres.in/api/users"
#     post_file = open("C:\\Auto\\API\\post2.json", "r")
#     read_post_file = json.loads(post_file.read())
#     post_result = requests.post(post_url, read_post_file)
#     print(post_result.text)
#     Id = jsonpath.jsonpath(post_result.json(), 'id')
#     print(Id[0])
#     assert post_result.status_code == 201

data1 = {
    "name": "morpheus",
    "job": "leader"
}


def test_ppost():
    a = requests.put("https://reqres.in/api/users/2", data1)
    print(a.status_code)
    print("123")

test_ppost()
# def test_putAPI():
#     put_url = "https://reqres.in/api/users/Id[0]"
#     put_file = open("C:\\Auto\\API\\put3.json", "r")
#     read_put_file = json.loads(put_file.read())
#     put_result = requests.put(put_url, read_put_file)
#     print(put_result.text)
#     assert put_result.status_code == 200
#
#
# def test_getAPI():
#     get_url = "https://reqres.in/api/users/" + str(Id[0])
#     get_result = requests.get(get_url)
#     print(get_result.text)
#     assert get_result.status_code == 200
#
#
# def test_delete_API():
#     delete_url = "https://reqres.in/api/users/Id[0]"
#     delete_result = requests.delete(delete_url)
#     print(delete_result.text)
#     assert delete_result.status_code == 204
#
#
# def test_getAPI1():
#     get_url = "https://reqres.in/api/users/Id[0]"
#     get_result = requests.get(get_url)
#     print(get_result.text)
#     assert get_result.status_code == 200
