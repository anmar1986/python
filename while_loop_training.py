admin = ["Anmar", "hussam", "Ayad", "Khalid"]

print(len(admin))

a = 0
while a < len(admin):
    print(f"#{str(a+1).zfill(3)} {admin[a]}")
    a +=1
else: print(" All of theme are printed")