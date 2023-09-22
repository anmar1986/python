myRange = range(1, 10)
for num in myRange:
    print(num)

mySkills = {
    "Html": "80%",
    "Css3": "50%",
    "PHP" : "76%",
    "JavaScript" : "90%",
    "Python" : "76%"
}

print(mySkills["Html"])
print(mySkills.get("Python"))

for skil in mySkills:
    print(f"my Progress in language {skil} is {mySkills[skil]}")
    print(f"my Progress in language {skil} is {mySkills.get(skil)}")