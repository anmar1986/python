# import sys 
# print(sys.path)
# sys.path.append(r"D:\Games")

from Module import firstM

print(dir(firstM))

firstM.sayHowAreYou("ANMAR")
firstM.sayHello("HUssAM")


print("_" * 100)
from Module import firstM as ee

print(dir(ee))

ee.sayHowAreYou("Karl")
ee.sayHello("Güenther")

