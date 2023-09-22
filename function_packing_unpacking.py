print(1, 2, 3, 4)
# artrisc print the elements in a list as a elements *args
mylist = [1, 2, 3, 4]
print(*mylist)


def say_hello(n1, n2, n3, n4):
    users = [n1, n2, n3, n4]
# instade of the array i can use the * astrisc to remove the array and user just the reference 
    for name in users:
        print(f"hello {name}")
say_hello("Anmar", "Hussam", "Bassil", "Ayad")

print("#" * 50)

def greeting(*items):
    for item in items:
        print(f"Hello Dear: {item}")
greeting("Jabsar Tiga", "Saman", "Chalack", "Koscher", "Basswienie Basher")


print("=" * 50)

def show_skills(name, *skills) :
        print(f"Hello {name} Your Skills Are:")
        for skill in skills:
            print(skill)
show_skills("AnMar", "Htms", "Css", "PHP", "Python")
show_skills("Hussam", "PHP", "java", "python", "mySql")







