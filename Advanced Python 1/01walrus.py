# Using walrus operator
l = [1, 2, 3, 4, 5]
if (n := len(l)) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)")
    