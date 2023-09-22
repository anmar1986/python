# index
a = "I Love Python And PHP"
print(a.index("P", 1, 10))
print(a.index("P", 1, 8))
print(a.index("P", 1, 10))
# rjust space and special characters
b = "Anmar"
print(b.rjust(10))
print(b.ljust(15), "###")

# cplitlines() split the lines to a list
e = """ First Line
    Second line 
    third Line"""
print(e)

print(e.splitlines())

f = """ First Line
    Second line 
    third Line"""
print(f.splitlines())
# tabs \t and i can expand them
g = "Hello\tWorld\tI\tlove\tpython"
print(g.expandtabs(11))

# is title
one = "I Love Python And 3G"
print(one.istitle())

# it the value is just a space
two = " i like you"
three = ""
print(two.isspace())
print(three.isspace())

# if lower case or no
four = "i like my uni"
five = "I LIke My uni"
print(four.islower())
print(five.islower())

# is identifier as a string or array
seven = "anmar_bahram"
eight = "100years"
print(seven.isidentifier())
print(eight.isidentifier())

# is alphabitical
x = "AAaaaaaBbbbbCccc"
y = "aaaabbbbccc10"
print(x.isalpha())
print(y.isalpha())

# alphabitical and numeric
u = "AAaaBBbbCCcc"
r = "65AAaaBBbbCCcc10"
print(u.isalnum())
print(r.isalnum())













