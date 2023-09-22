# built In Function
# enumerate()
# hel()
# reverse()

mySkills = ["PHP", "Python", "JavaScript", "Mysql", "Git"]

myskCount = enumerate(mySkills, 100)
for counter, skill in myskCount:
    print(f"{counter} - {skill}")

print("_" *50)


print(help(print)) # Help is explain evreything 

print("=" * 50)
myString = "Anmar Albahramani"
print(reversed(myString))

for letter in reversed(myString):
    print(letter)

