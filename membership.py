admin = ["Anmar", "Karl", "Markus","Lydia", "Kusch"]

name = input("Please writ your name: ").strip().capitalize()

if name in admin: 
    print(f"Hello {name} welcome back")
elif name not in admin:
    option = input("Delete or Update Your Name ").strip().capitalize()
    if  option == "update":
        theNewName = input("Your New Name: ").strip().capitalize()
        print(theNewName)
        admin[admin.index(name)] = theNewName
else:
    print("You Are Not Admin!")