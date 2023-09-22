# Dictionary

# => key -> value
# => key should be uniqu
# => i can get the value by the key not by index
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