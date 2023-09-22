# email = "anmar.bahram@gmail.com"
# print(email[:email.index("@")])

name = input("What Is Your Name ?").strip().capitalize()
mail = input("What Is Your Mail ?").strip()

theName = mail[:mail.index("@")]
theMail = mail[mail.index("@")+1:]

print(f"Your Name Is: {name} And Your E-mail Is: {mail}")
print(f"Your UserName Is: {theName} \n && Your website Is: {theMail}")

