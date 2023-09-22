uName = "Anmar"
cName = "Python Course"
country = ""
cPric = 100
cDisc = [20, 30, 50]

input("Print your Country:")

if country == "Irak":
    print(f"Hello {uName} the course \"{cName}\" price is ${cPric - cDisc[0]}")
elif country == "Austria":
    print(f"Hello {uName} the course \"{cName}\" price is ${cPric - cDisc[1]}")
else:
    print(f"Hello {uName} the course \"{cName}\" price is ${cPric - cDisc[2]}")