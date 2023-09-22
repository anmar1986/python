# Map builtin funcion

# => map take a function and iterator 
# => map caled map because it map the function on evrey element
# => the function can be pre defined function or lambda function
def formatText(text):
    
    return f"- {text}"

myTexts = ["Anar", "Hussam", "Anad", "Julia"]
#1
myFormatedData = map(formatText, myTexts)

#print(myFormatedData)
for item in myFormatedData:
    print(item)
#2
for user in map(formatText, myTexts):
    print(user)

for index in list(map(formatText, myTexts)):
    print(index)

print("=" *50)

for name in list(map(lambda text: f"{text.strip().capitalize()} -", myTexts)):
    print(name)
