# => list items are enclosed in Square Brackets
# => list is not unique 
# => list is zero index
# => list can have different data typer
myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(myList)
print(myList[1:4])
print(myList[:3])
print(myList[4:])

mylist1 = [0, 1, "Anmar", "Two" , ["one", "two", "three"], 1.2, True, False]
print(mylist1[4][2])
print(type(mylist1[4][2]))
print(type(mylist1[0]))
print(type(mylist1[2]))
print(type(mylist1[5]))
print(type(mylist1[6]))
print(mylist1[::1]) # => jumping  new no jump
print(mylist1[::2]) # => jumping 2 elements
print(mylist1[::3]) # => jumping 3 jump

myList[0] = 250 # => mutable i can change the value in the runtime.
print(myList)
