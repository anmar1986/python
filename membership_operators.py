name = "Anmar"

print("m" in name)
print("n" in name)
print("r" in name)
print("M" in name)

print("#" * 50)

friends = ["Anmar", "Markus", "Kusch", "Lydia", "Mani"]
print("Mani" in friends)
print("Jan" not in friends)
print("hussam" not in friends)

print("**" * 50)

count = ["Irak", "Iran", "Syria", "Lebanon"]
disco = ["20%", "30%", "40%", "50%"]

co = input("what is your country ?: ")

if co  in count:
    print(f"your discount is {disco[3]}")
elif co not in count:
    print(f"your discount is {disco[0]}" )