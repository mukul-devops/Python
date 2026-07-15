class Employee: 
    language = "Py"       # This is a class attribute
    salary = 1200000
    def getinfo(self):    #self refers to the object
        print(self.name,self.language)
      


harry = Employee()
harry.name = "Harry"      # This is an instance attribute
print(harry.name, harry.language, harry.salary)
harry.getinfo()           #same as Employee.getinfo(harry)
