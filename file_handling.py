# "a" => append open file for appending values create file if not exists
# "r" => read [default value] open file or read and give error if file not exist
# "w" => write open file for writing, create file if not exist
# "x" => create fiel , give error if file not exist

#files = open("file", "mode") 
#fiel=>  path,  mode=> one of thin a r w x

# absulute path 
# relativ path # where am i

#fiel = open("C:\xampp\htdocs\python\Bewerbung.txt", )
import os 
print(os.getcwd()) # Main current working directory
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__))) # directory for the opend file

# change current working dirctiory 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file = open(r"c:\xampp\htdocs\python\anmar.txt")