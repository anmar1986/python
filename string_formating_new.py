myStr = "My Name Is Anmar I Am 37 years Old I Am Living Acctully In Vienna"
myString = "Hello Users I am Anmar"
myAge = 37
Keto = 45


print("This Is My Message: {:s} and age is {:d} and keto is {:f} " .format(myString, myAge, Keto))

# ReArrange Items

a, b, c = "Anmar", "Hussam", "Bassim"

print(" {} {} {}" .format(a, b, c))
print(" {2} {1} {0}" .format(a, b, c))
print(" {1} {2} {0}" .format(a, b, c))

x, y, z = 10, 20, 30

print("{} {} {}" .format(x, y, z))
print("{0:d} {1:f} {1:f}" .format(x, y, z))
print("{1} {0} {2}" .format(x, y, z))
print("{0:d} {1:.4f} {1:.1f}" .format(x, y, z))

myName = "Anamr "
myAges = 37

# new formating way in 3.6 python the best way
print(f"My Name Is: {myName} nad my age: {myAge}")