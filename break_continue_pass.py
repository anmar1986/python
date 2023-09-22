numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num == 5: 
        continue # continue will jump this number or iteration and continue
    print(num)

print('#' * 50)

for item in numbers:
    if item == 6:
        break # the break will stop and not continue 
    print(item)


print('=' * 60)

for _item in numbers:
    if _item == 2: # will print nothing except number 2 in this example
        pass
        print(_item)