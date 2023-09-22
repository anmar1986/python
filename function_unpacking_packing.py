mydict = {
    "php" :"89%",
    "python": "78%", 
    "javascript": "65%",
    "MySQL": "66%"
}
mytuple = ("PHP", "Python", "JavaScipt")
def show_skills(name, *skills, **skillsWithProgress):
    print(f"Hello{name} \nskills without progress is ")
    for skill in skills:
        print(f" -{skill}")
        print("Skills with progress is ")
        for key, value in mydict.items():
            print(f"{key } => {value}")
show_skills("Hussam", *mytuple, **mydict)