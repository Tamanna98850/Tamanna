### File Handling

# Python can read and write files.

## Write
# file = open("data.txt", "w")
# file.write("Hello Python")
# file.close()

## Read
# file = open("data.txt", "r")
# data = file.read()
# print(data)
# file.close()

## Recommended Method
# with open("data.txt", "r") as file:
#     data = file.read()
#     print(data)