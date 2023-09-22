uName = "Anmar"
cName = "Python Course"
country = ""
age = ""
cPric = 100
cDisc = [20, 30, 50]

input("Print your Country:")
input("write your age please")
if country == "Irak":
    print(f"Hello {uName} the course \"{cName}\" price is ${cPric - cDisc[0]}")
elif country == "Austria":
    print(f"Hello {uName} the course \"{cName}\" price is ${cPric - cDisc[1]}")
else:
    print(f"Hello {uName} the course \"{cName}\" price is ${cPric - cDisc[2]}")