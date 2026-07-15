class Employee:
    def __init__(self,name):
       self.name = name
       
    @property                                 #getter to get (read) value
    def name(self):
       return f"{self.fname} {self.lname}" 
    @name.setter                              #setter to set (change) value
    def name(self,value):
       self.fname = value.split(" ")[0]
       self.lname = value.split(" ")[1]

e = Employee("mukul chahar")
e.lname = "Jaat"                              
print(e.name)