
print("#" * 50)
print("you can write just the first letter of the time uni as example w for weeks and m for months and y for years".center(50, "#"))
print("#" * 50)

age = input("Writ your age please: ").strip()

unit = input("please choose time unit: Months Weeks Days : ").strip().lower()

print(unit)


months = int(age) * 12
weeks  = months * 4
days   = int(age) * 365

if unit == "Months" or unit == "m" or unit == "M":
    print("You choose months...")
    print(f"you lived vou {months:,} months")
elif unit == "Weeks" or unit == "w" or unit == "W":
    print("You choose weeks...")
    print(f"you lived vou {weeks:,} weeks")
elif unit == "Days" or unit == "D" or unit == "d":
    print("You choose days ")
    print(f"Your age in days is {days:,}")


