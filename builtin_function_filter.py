# => filter take a function and iterator
# => filter run a function on every element
# => the function can be pre-defined function or lambda function
# => filter out all elements for which the function teturn true
# => the function need to return Boolean value

def checkNumber(num):
    if num > 10:
        return num
    ## important return Trun 
    # i can make it also like (    if num == 0 return True  ) because if i return the number 0 it is False and will not be printed

myNumbers = [1, 2, 3, 10, 11, 15, 45, -103, 0]

for number in filter(checkNumber, myNumbers):
    print(number)



print("#" *40)
print("#" *40)

# Example 2

def checkName(name):
    return name.startswith("A")

myText = ["Anmar", "Ahmed", "arkan", "Osama"]

for name in filter(checkName, myText):
    print(name)
print("_" *40)
print("-" *40)

myText = ["Anmar", "Ahmed", "arkan", "Osama"]


for name in filter(lambda name: name.startswith("A"), myText):
    print(name)
