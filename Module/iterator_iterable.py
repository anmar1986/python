# iterable => string tuple dictionary list 
# iterator => for a in b : , 

name = "Anmar"
mylist = [1, 2, 3, 4, 5]
for index in name:
    print(index)
    print(index, end=" ")

for item in mylist:
    print(item)
    print(item, end=" ")

print("_" * 100)

# iterator iter() method

myIterator = iter("anmar")
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))