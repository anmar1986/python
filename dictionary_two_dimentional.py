user = {
    "name": "Anmar",
    "age": 34,
    "country": "Iraq",
    # list is not acceptable but the set will be accepted
    (1, 2, 3, 4) : "True",
    23: "Yes",
    "order": ["Html", "Css", "PHP"],
    "rating": 1.4,

}

print(user["country"])
print(user.get("country"))
print(user.keys())
print(user.values())

print("#" * 50)

languages = {
    "One" : {
        "name": "Html", 
        "progress": "89%"
    },
    "Two" : {
        "name": "PHP",
        "progress": "67%"
    },
    "Three": {
        "name": "JavaScript",
        "progress": "67%"
    }
}
print(languages)
print(languages.keys())
print(languages.values())
print(languages["One"])
print(languages["Two"]["progress"])
print(len(languages))
print(len(languages["Two"]))


print("*" * 100)
fwOne = {
    "name": "VueJs",
    "progress": "50%"
}

fwTwo = {
    "name": "React",
    "progress": "40%"
}

fwThree = {
    "name": "Angular",
    "progress": "30%"
}

allfw = {
    "one": fwOne,
    "two":fwTwo,
    "three": fwThree
}

print(allfw)