# clear()
user = {
    "name": "anmar",
    "age" : "37 years"
}
print(user)
user.clear()
print(user)

print("#" * 50)

# update()
member = {
    "name" : "Anmar",
    "Age" : "37 years"
}
print(member)
member["Age"] = "31 Years"
print(member)
member.update({"name": "Hussam"})
print(member)
member.update({"country": "Iraq"})
print(member)

# copy
print("|" * 300)
main = {
    "name": "anmar", 
    "age": "34"   
}
b = main.copy()
print(main)
print(b)
main.update({"address": "iraq"})
print(main)
print(b)
print(main.keys())
print(main.values())