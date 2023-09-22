skills = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for skill in skills: 
    print(f"{skill} => {skills[skill]}")

print("#" *30)

for key, value in skills.items():
    print(f"{key} => {value}")

    
print("#" *50)

uSkills = {
    "backend": {
        "PHP": "70%",
        "Python": "60%",
        "MySQL": "67%"   
    },
    "frontend": {
        "JavaScript": "65%",
        "React": "60%",
        "Vue.sj": "78%",
        "Html": "89%",
        "CSS3": "87%"
    }
}

for xkey, yval in uSkills.items():
    print(f"{xkey} Progress is: ")
    for child_key, child_value in yval.items():
        print(f" -{child_key} => {child_value}")