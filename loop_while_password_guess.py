tries = 3
mpass = "anmar1985"

inputPass = input("write your password please: ")

while inputPass != mpass:
    tries -=1
    print(f"wrong password, { 'last' if tries == 0 else tries} your havae juon one chance")
    inputPass= input("wirte Pss agein: ")
    if tries == 0: 
        print("all your tries are finished")
        break
print("will not be filled")
