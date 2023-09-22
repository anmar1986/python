import datetime

mybd = datetime.datetime(1986, 4, 10)

print(mybd.strftime("%A"))
print(mybd.strftime("%B"))
print("_" * 50)
print(mybd.strftime("%x"))
print(mybd.strftime("%B"))

print("_" * 50)
print(mybd.strftime("%Y"))
print(mybd.strftime("%A %B %x %Y"))
