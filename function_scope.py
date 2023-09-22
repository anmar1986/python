x = 2
def  one():
    global x
    x = 34
    print(f"my value {x}")

def  two():
    print(f"my value {x}")


one()
print(x)
two()