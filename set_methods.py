t = {2, 4, 6, "Anmar", "Bahram"}
t.clear()
print(t)

# union()
a = {2, 4, 6, "Anmar", "Bahram"}
b = {"Hussam", "Basseil"}
print( a | b)
print(a.union(b))

# add()
d = {1, 2, 3}
d.add(78)
d.add(3443)
print(d)

# copy() not deep copy its just schalow copy
e = {1, 2, 3, 4, 5}
f = e.copy()
print(e)
print(f)
e.add(90)
print(f)

g = {1, 2, 3, 4}
g.remove(1)
print(g)
# g.remove(34)

# discard
h = {1, 2, 3, 4}
h.discard(1)
print(h)
h.discard(34)

# pop rundum remove a element but i can not choose the element
i = {1, 2, 3, "yes", True, False, 12.12}
i.pop()
print(i)

# update() will remove the ununice elements

j = {1, 2, 4, 5, 6, 7}
k = {"hello", 1, 2, 3, 4, 5, 6, "hussam", "why", "I ", "and"}
j.update(k)
print(j)

