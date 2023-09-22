# => append
myList = [1, 2, 3, "Anamr", "Hussam"]
myList1= ["one", "two", "three"]
myList.append(True)
myList.append(False)
myList.append("ayad")
myList.append(10.05)
myList.append(myList1)
print(myList)
print(myList[9][2])
print(myList[9])

# => extend
myLists = [1, 2, 3, "Anamr", "Hussam"]
myLists1= ["one", "two", "three"]

# remove just one element
myLists.extend(myLists1)
print(myLists)
myLists.remove('Hussam')
print(myLists)

# sort by default sort(reverse=false)
y = [1, 2, 3, 100, -29, -1,  0,  33]
y.sort(reverse=True)
print(y)

# reverse
x = [1, 2, 3, 10 , 9, 80, "on"]
x.reverse()
print(x)