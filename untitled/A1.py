import jsonpath

e={
    "employees": [{
        "name": "Shyam",
        "email": "shyamjaiswal@gmail.com"
    }, {
        "name": "Dhanraj",
        "email": "raj@gmail.com"
    }, {
        "name": "Dhanshree",
        "email": "shree@gmail.com"
    }]
}

# print(e[employees])




# try:
#     a = 3/0
#     raise someerror
# someerror:
#     print("can not devide 0 by 3")
# except:
#     print("can not devide 0 by 3123")



s = "selenium is a tool and selenium used for web applications automation";
# seleniuM iS A tooL anD seleniuM useD foR weB applicationS automatioN
s = s.split()
print(s)
s1 = ""
n = 0
for i in s:
    i = i[0:-1].lower() + i[-1].capitalize()
    s1 += i + " "
print(s1)


