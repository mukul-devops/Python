l = [23,5,55,27,50,990,67,87]
def diviby5(n):
    if n%5==0:
        return True
    return False
a = filter(diviby5,l)

print(list(a))

