# is subset
a = {1, 2, 3, "Yes", True, False}
b = {1, 2, 3, "Yes", True, False, "NO"}
print(a.issubset(b))

print("|" * 100)
# issuperset()
c = {1, 2, 3}
d = {1, 2, 3, 4, 5}
print(c.issuperset(d))

print("|" * 100)

g = {1, 2, 3, 4}
h = {45, 56, 67.3, 789}
print(g.isdisjoint(h))