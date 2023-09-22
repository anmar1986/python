a = "my name is anmar "
b = "i-love-php-and-python"
c = "i-love-java-and-javascript-and-mysql-and-git"
# split() rsplit() return a list
print(a.split()) # split from the space by default
print(b.split("-")) # split from the -
print(c.split("-", 2)) # from right side
print(c.rsplit("-", 5)) # from left side

# Center
d = "my name is anmar"
print(len(d))
print(d.center(22, "@"))
# count the nember of the patern or text which im looking for 
e = "i love python and pyrix and because i php and php love java and java and php and another php"
print(len(e))
print(e.count("py"))
print(e.count("php", 0, 66))
# swap capital to small and smal to capital
print(e.swapcase())

# startswith
print(e.startswith("i")) # ture

print(e.startswith("j", 55)) # true
print(e.startswith("j", 55, 60)) # true
print(e.endswith("p")) # true
print(e.endswith("k")) # false