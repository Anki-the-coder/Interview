"""
With / As Keywords
"""
# print("Normal Write Start")
# my_write = open("textfile.txt", "w")
# my_write.write("Trying to write to the file")
# my_write.close()
#
#
# print("Normal Read Start")
# my_read = open("textfile.txt", "r")
# print(str(my_read.read()))

print("With As Write Start")
with open("withas.txt", "w") as with_as_write2:
    with_as_write2.write("This is an example of with as write/read by Anki")

print()
print("With As Read Start")
with open("withas.txt", "r") as with_as_read1:
    print(str(with_as_read1.read()))
