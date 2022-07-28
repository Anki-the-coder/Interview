"""
Examples to show available string methods in python
"""

# Replace Method
a = "a1bc2abcd3abc4abc"
print(a.replace('abc', 'ABC'))

# Sub-Strings
# starting index is inclusive
# Ending index is exclusive
sub = a[1:6]
step = a[1:6:2]

print("****************")

print(sub)
print(step)