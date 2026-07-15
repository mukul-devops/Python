def replace(word):
    with open("file.txt") as f :
        content = f.read() 
        content= content.replace(word,"####")
    with open("file.txt","w") as f:
        
        f.write(content)
       
      
replace("donkey")

       
       
      
    
    
