# abs()
# pow()
# min()
# max()
# slice()

print(abs(100))
print(abs(-100))
print(abs(100.102))
print(abs(-100.102))
print("#" * 50)

print(pow(2, 10)) #=> 2 * 2 * 2 *2 *2 * 2 * 2 * 2 * 2 * 2
print(pow(2, 5 , 6)) # =>  2 * 2 * 2 * 2 * 2 * 2 % 
print("-" * 50)

print("*" * 50)
mylist = (1, 44, 66, -10)
print(min(mylist))
print(max(mylist))
print("*" * 50)
print(min(100, 10, 30, -30))
print(min("A", "B", "T", "Anmar"))
print(max(1, 23, 90, -11.2))
print(max("A", "B", "T", "Anmar"))


print('#' *100)
a = [1, 2, 3, 4,55, 65,5]
print(a[:2])
print(a[slice(1,3)])