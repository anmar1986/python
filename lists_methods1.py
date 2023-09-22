a = ["one", "two", "three", 1, 2, 3, "A", "B", "C"]
a.clear() # => make the list empty
print(a)

b = ["one", "two", "three", 1, 2, 3, "A", "B", "C"] # => main list
c = b.copy() # copied list schalow copy
b.append(34)
print(b)
print(c)

# count just counts the number of an element
d = [1, 2, 3, 3, 3, 11, 11, 39, "Ramy"]
print(d.count(11))
# index search the index of the element
print(d.index("Ramy"))
print(d.index(11))

# insert 
f = [1, 2, 3, "a", "b", "c"]
f.insert(0, "Test")
f.insert(-1, "Yes")
print(f)

# pop remove a element when i support him with the index of the element
g = [1, 2, 3, 'Yanko', 'Iris']
g.pop(2)
g.pop(-1)
print(g)