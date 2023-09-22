a, b, c = "anmar", "Hussam", "Basil"

# print(f"Hllo {a}")
# print(f"Hllo {b}")
# print(f"Hllo {c}")
# def           => function key word
# say_hello()   => function name
# name          => parameter
# 
def say_hello(name):

    print(f"Hello {name}")

#say_hello(a)

def addition(n1, n2):
    print(n1 + n2)
#addition(-10, 30)
print("=" * 100)
def sup(n1, n2, n3):
    if type(n1) != int or type(n2) != int or type(n3) != int:
        print("only integer numbers are allowed")
    else:
        print(int(n1) + int(n2) + int(n3))

#sup(1, 2, 10)



def full_name(fName, mName, lName ):
    print(f"Hello {fName.strip().capitalize() } {mName.upper():.1s} {lName.capitalize()}")
full_name("  Anmar", "Moffaq", "Albahramani")


