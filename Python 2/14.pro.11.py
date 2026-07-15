with open("old.txt") as f:
    content = f.read()
with open("renamed_by_python.txt","w") as f:
    f.write(content)

#delete the old.txt with the help of module (os , shutil)