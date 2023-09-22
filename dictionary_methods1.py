# set default
user = {
    "name": "Anmar", 
    "address": "Wien",
    "skills": "PHP, Python"
}
print(user)
print(user.setdefault("city", "Hussam"))
print(user)

print("#" *40)

# popitem

item = {
    "name": "anmar", 
    "age" : "44",
    "city": "bagdag"
}
print(item)
item.popitem()
print(item)

# items
print("0" * 100)
view = {
    "name": "amar",
    "age": "44"
}
print(view)
alli = view.items()
print(alli)

# fromkeys()
print("*" * 100)

a = ("keyone", "keytwo", "keythree")
b = "x"

#create a dictionary from the keys and the values which i support
print(dict.fromkeys(a, b))