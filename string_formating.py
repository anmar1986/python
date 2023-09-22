name = "Anmar"
age = 34
rank = 11

print("My Name Is: " + name)
# print("My Name Is; " + name " And My Age Is: " + age + "And My Rank Is " + rank)
print("My Name Is: %s" % name)
print("My Name Is: %s  And My Age Is: %d And My Rank Is %f" % (name, age, rank))

# Placeholder
# %s => string
# %d => number 
# %f => float
n = "Anmar "
l = "Python" 
y = "Years"
print("im %s and my languages is %s and im 44 %s old" %(n, l, y))

myNumber = 10

print("My Number Is: %d" %myNumber)
print("My Number Is: %f" %myNumber)
print("My Number Is: %.3f" %myNumber)

myLongString = "Hello My Comunity"
print("My Message Is: %s" % myLongString)
print("My Message Is: %.10s" % myLongString)