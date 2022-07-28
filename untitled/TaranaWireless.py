# Write a function to find the characters repeated consecutively in the given string.
# Get the value for how many times the same character is repeated.

s = "zookeeepper"
d = {}
for i in range(len(s)-1):
    if str(s[i]) == str(s[i+1]):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 2

print(d)
