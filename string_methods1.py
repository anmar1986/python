myString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
myStr    = "    I Love Python    "
print(len(myStr))
print(len(myString))
# strip() rstrip() lstrip() len()

print(myStr.strip())
print(myStr.rstrip())
print(myStr.lstrip())

a = "#### i love php ####"

print(a.strip('#'))
# Title all the first leters of the words will be capital letter
b = "i love 2d and 3d graphics and technology and Python"
print(b.title())

# just the first word in the sentence will start with capital letter
print(b.capitalize())

x = "hello world"
print(x.capitalize())

# zfill
c, d, e = "1", "11", "1111"

print(c, d, e)
print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
# upper lower
print(b.upper())
print(b.lower())