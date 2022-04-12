import os

list = os.listdir()

for file in list:
    if file == "README.md":
        list.remove(file)
    if file == "script.py":
        list.remove(file)

for file in list:
    os.system("echo ![image]\("+ file + "\) >> README.md")

