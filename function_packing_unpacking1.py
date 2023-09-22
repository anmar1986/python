# kwargs

# def show_shills(*skills):
#      #   print(type(skills))
#         for skill in skills:
#             print(skill)
# show_shills("PHP", "Python", "JavaScript", "MySQL")
mydict = {
    "php" :"89%",
    "python": "78%", 
    "javascript": "65%",
    "MySQL": "66%"
}
def show_shills(**skills):
     #   print(type(skills))
        for skill, value  in skills.items():
            print(f"{skill} => {value}")
show_shills(**mydict)

