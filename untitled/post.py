import json
import requests

# baseURL2 = "https://reqres.in/api/users"
# file = open('C:\\Auto\\API\\Post1.json', 'r')
# json_input = file.read()
# request_Json = json.loads(json_input)
# posted = requests.post(baseURL2, request_Json)
# # print(posted)
# # print(posted.text)
# print(posted.content)
# assert posted.status_code == 201


# baseURL3 = "https://reqres.in/api/users/2"
# file3 = open("C:\\Auto\\API\\Post1.json", "r")
# json_input3 = file3.read()
# json_request3 = json.loads(json_input3)
# updated = requests.put(baseURL3, json_request3)
# print(updated.text)

deleteURL = "https://reqres.in/api/users/2"
delete_request = requests.delete(deleteURL)
print(delete_request.content)



