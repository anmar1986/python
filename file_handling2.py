# myfile = open(r"C:\xampp\htdocs\Python\test.txt", "w")
# myfile.write("Hello I Am Writing From File outsid\n")
# myfile.write("Second File\n")

# myfile = open(r"C:\xampp\htdocs\Python\testing.txt", "w")
# myfile.write("ANm ar \n" * 100)

mylist = ["Anmar\n", "Hussam\n", "Bashar\n"]
myfile = open(r"C:\xampp\htdocs\Python\fun.txt", "w")
myfile.writelines(mylist)
myfile.write("My new Line\n")
myfile.write("This is new Line\n\n\n\n\n")