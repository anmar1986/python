# all()
# any()
# bin()
# id()

numbers = [1, 2, 3, 4, 5] # all elements are exists
if all(numbers) :
    print("All Elements Are Trun")
else:
    print("One Of Them Is Empty")

num = [1, 2, [], 4, 5] # empty element
if all(num) :
    print("All Elements Are Trun")
else:
    print("One Of Them Is Empty")    

print('#' * 50)


x = [1, 2, [], 4, 5]
if any(x) :
    print("one element is true ")
else:
    print("no element is true")

y = [0, []]
if any(y) :
    print("one element is true ")
else:
    print("no element is true")

print("=" * 50)

print(bin(1))
a = 1
b = 2
c = 10
print(id(a))
print(id(b))
print(id(c))