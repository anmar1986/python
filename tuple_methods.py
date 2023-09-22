a = ("a",)
b = "bcd",
print(type(a))
print((a))

print(type(b))
print((b))

# tuple concation
c = (2, 3, 4)
d = (1, 5, 7)
e = c + ( "a", "b", "c") + d 
print(e)

# repeat 
myStr = "ANMAR"
myList = ["A", "B ", "C"]
myTuple = ("K", "L")
print(myStr * 5)
print(myList * 4)
print(myStr * 10)

# count
k = (1, 2, 3, 4, 5, 6, 7, 8)
print(k.count(7))

# index

l = (1 ,2, 33, 4)
print("This is your value: {:d}" .format(l.index(4)))
print(f"the index of your element: {l.index(4)}")

val = ("A", "B", 45, "C")
z, y, _ , s = val
print(s)
print(z)
print(y)