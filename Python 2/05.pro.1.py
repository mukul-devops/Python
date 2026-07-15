with open("poem.txt") as f:
    content = f.read()
    
if("Twinkle" in content):
    print("it contain twinkle")
else:
    print("it not contain twinkle")    