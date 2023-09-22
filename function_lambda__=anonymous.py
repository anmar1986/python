# - Function Lambda 
# - Function Anonymous

# Has No Name
# We Can Call It Inline Withou Define It
# We Can Use It In Return Data From Another Function
# Lambda Used For Simple Functions And Def Handle The Large Tasks 
# Labbda Is One Singel Expression  Not Block Of Code
# Lambda Type Is Function

def sayHello(name, age): return f"Hello {name.lower()} your age is: {age}"

hello = lambda name, age : f"Hello {name.lower()} Your Age Is : {age}:"

print(sayHello("Namar", 34))
print(hello("Hussam", 33))

print(sayHello.__name__)
print(hello.__name__)

print("# " * 50)

exp = lambda x, y : f"your naem is {x} and age is {y}"
print(exp("Nammmmmer", 55))