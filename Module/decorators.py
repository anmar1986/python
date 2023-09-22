# Decorator => called sometimes Meta programming
# all the data in python is object
# Decorator takes a function and add some Decoretors and return it
# Decorator Wrap other function and enhance there Beaviour
# it is a Heigher order Function 

def myDecoratior(func):

    def nestedFunc():

        print("Before ")

        func()

        print("After")

    return nestedFunc
