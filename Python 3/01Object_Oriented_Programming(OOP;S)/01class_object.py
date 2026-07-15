class Employee: 
    language = "Py" # This is a class attribute
    salary = 1200000


harry = Employee()     #Object Instantiation
harry.name = "Harry" # This is an instance attribute
print(harry.name, harry.language, harry.salary)

Employee.language = "c"   #changing class attribute

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class