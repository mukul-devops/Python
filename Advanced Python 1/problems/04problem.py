try:

    a = int(input("enter a no:"))
    b = int(input("enter a no:"))    
    print(a/b)

    
except ZeroDivisionError:
    if(b==0):
        print("it is infinity")

