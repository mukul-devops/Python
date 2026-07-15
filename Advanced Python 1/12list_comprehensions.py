'''
list comprehensions are a concise way to create lists in Python. 
They allow you to generate a new list by applying an expression to each item in an existing iterable (like a list, tuple, or string) 
and optionally filtering items based on a condition.
'''
myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

squaredList = [i*i for i in myList]

print(squaredList)


list1 = [1,7,12,11,22] 
list2 = [item for item in list1 if item > 8] 
print(list2)

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
result = [a + b for a, b in zip(l1, l2)]
print(result)  # Output: [6, 8, 10, 12]