import json
import sys
import requests

baseURL1 = "https://www.facebook.com/friends/?profile_id=100054354240642"
baseURL2 = "https://reqres.in/"

resp1 = requests.get(baseURL1)
# print(resp1.content)

resp2 = requests.head(baseURL1)
# print(resp2.content)

resp3 = requests.options(baseURL1)
# print(resp3.headers)

resp4 = json.loads(resp1.text)
# print(resp4)

# struct = {}
# try:
#     resp4 = str(resp1.text).strip("'<>()").format('\'', '\"')
#     struct = json.loads(resp4)
# except:
#     print(repr(resp1))
#     print(sys.exc_info())
#     print("this is exception")

# print(resp4)

resp_Post = requests.get(baseURL2)
resp5 = json.loads(resp_Post.text)
file = open("C:\\Auto\\API\\post1.txt", "r")
upload = requests.post("https://reqres.in/api/users", "file")
print(upload.status_code)






