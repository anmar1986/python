myFile = open(r"c:\xampp\htdocs\python\test.txt")
# print(myFile) # data object 
# print(myFile.name)
# print(myFile.mode)
# print(myFile.encoding)

print(myFile.read(10))
print('#' *25)
print(myFile.readline())
print('#' *25)
print(type(myFile.readlines()))

for line in myFile:
    print(line)

    if line.startswith("ch"):
        break

myFile.close()