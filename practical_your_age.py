age = int(input('What Is Your Age ? ').strip())
print(age)
print(type(age))

months = age * 12
weeks  = months * 4
days   = age * 365
hours  = days * 24
minute = hours * 60
seconds = minute * 60

print("You Live For: ")
print(f"months: {months}")
print(f"weeks: {weeks:,}")
print(f"days: {days:,}" )
print(f"hours: {hours:,}")
print(f"minute: {minute:,}")
print(f"seconds: {seconds:,}")
