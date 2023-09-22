###### Reduce ######
# => reduce take a function and iterator
# => reduce run a function on first and second element and give result
# => and then run function on result and thierd element
# => and then run function on result and forth element and so on
# => Till one element is is left and then:  this is the result
# => the function could be lambda or pre defined function

from functools import reduce


def sumAll(num1, num2):
    return num1 + num2 

numbers =  [1, 2, 3, 4, 5]

print(reduce(sumAll, numbers))


print("=" * 50)


numbers =  [1, 2, 3, 4, 5]

print(reduce(lambda num1, num2: num1 + num2, numbers))

