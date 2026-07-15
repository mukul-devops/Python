try:
    with open("f1.txt") as f:
        print(f.read())
except Exception as e :
    print(e)


try:
    with open("f2.txt") as f:
        print(f.read())
except Exception as e:
    print(e)
    

try:
    with open("f3.txt") as f:
        print(f.read())
except Exception as e:
    print(e)

print("thank you")