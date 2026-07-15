def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

        
    except Exception as e:
        print(e) 
        return


    finally:                                 #this is always executed in any condition
        print("Hey I am inside of finally")


main()