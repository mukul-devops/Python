try:                                         #this allow to run a program without crash
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("Heyyyy")
    print(v)
    
except Exception as e:       # All other exceptions are handled here. 
    print(e) 

print("Thank You")