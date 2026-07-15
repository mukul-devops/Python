def replace(l):
    with open("file.txt") as f :
        content = f.read()
    for word in l:
        content= content.replace(word,"#"*len(word))

    with open("file.txt","w") as f:
        
        f.write(content)
       
      
l= ["donkey","bad","spam"]
replace(l)
