# users = ["Anmar", "Hussam","Bassil", "Ayad", "Kusch", "Lydia"]
# skills = ["PHP", "Python", "JavaScript", "Java", "MySQL"]

# for user in users :
#     print(f"{user} skills is: ")
#     for skill in skills:
#         print(f"{skill} ")


peoples = {
    "Anmar": {
        "PHP": "67%",
        "JavaScipt": "78%",
        "Python": "87%"
    },
    "Hussam": {
        "PHP": "98%",
        "JavaScipt": "95%",
        "Python": "60%"
    },
    "Ayad": {
        "PHP": "67%",
        "JavaScipt": "60%",
        "Python": "82%"
    }
}

for peo in peoples:
    print(f"{peo} skills is:")
    for skill in peoples[peo]:
        print(f"{skill} => {peoples[peo][skill]}")
        # print(skill)
