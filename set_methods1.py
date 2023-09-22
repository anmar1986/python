# => difference()
a = {1, 2, 3, 4}
b = {1, 2, 3, 6, 7}
print(a)
print(a.difference(b))


print("=" * 50)
# => difference_update()
c = {1, 2, 3, 4}
d = {1, 2, 3, "Anmar", "Hussam"}
print(c)
c.difference_update(d)
print(c)

print("#" * 100)
# => intersection() The elements which exist in the booth sets
e = {1, 2, 3, 4, "X"}
f = {"Anmar ", "X", 2}
print(e)
print(e.intersection(f))
print(e)

print("*" * 100)
# intersection_update()
g = {1, 2, 3, 4, "X", "Anmar"}
h = {"Anmar", "X", 2}
print(g)
g.intersection_update(h)
print(g)

print("_" * 50)
# symmetric_difference()
x =  {1, 2, 3, "Anmar", "Hussam"}
y =  {1, "Hussam"}
print(x)
print(x.symmetric_difference(y))


print("_|" * 50)
# symmetric_difference()
k =  {1, 2, 3, "Anmar", "Hussam"}
l =  {1, "Hussam"}
print(k)
k.symmetric_difference_update(l)
print(k)