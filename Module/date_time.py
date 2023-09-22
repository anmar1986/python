# DateTime Introdution

import datetime
print(dir(datetime))
print("_" *100)

print(datetime.datetime.now())
print("_" *100)

print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print("_" *100)

print(datetime.datetime.min)
print(datetime.datetime.max)
print("_" *100)


print(datetime.datetime.now().time().hour)
print(datetime.datetime.now().time().minute)
print(datetime.datetime.now().time().second)
print("_" *100)

print(datetime.datetime(1986, 4, 10))
print(datetime.datetime(1986, 4, 10, 10, 10, 10))
print("_" *100)

birthday = datetime.datetime(1986, 4, 10)
datenow  = datetime.datetime.now()
print("_" *100)

print(f"You age is: {datenow - birthday}" )