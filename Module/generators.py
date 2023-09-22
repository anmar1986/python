# is a function use yield keyword instade of return 

def myGenerator():
    yield 1 
    yield 2
    yield 3
# print(myGen())

myGen = myGenerator()
print("Just a test text") 
print(next(myGen))
print(next(myGen))
print("Just a test text") 
print(next(myGen))
print('#' *50)

for number in myGenerator():
    print(number)