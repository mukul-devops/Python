from functools import reduce
l = [34,45,34,69,97,5,37,76]
def greater(a,b):
    if a>b:
        return a
    return b

a = reduce(greater,l)
print(a)