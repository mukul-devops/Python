class Student:
    salary = 1200000
    language = "python"

    @staticmethod
    def greet():                        #It doesn't need self parameter value
        print("Good morning")


    def __init__(self, name,language):  #dunder meathod which called automatically when object is created
        self.name = name                #it also set arguments as instance attributes
        self.language =language         
        print("I am creating an object")

    def display(self):                  #self refers to the object
        print(self.name,self.language)

s = Student("Mukul","python")           #Instantiation of object1
s.greet()
s.display()

o = Student("karan","java")             #Instantiation of object2     
o.greet()
print(o.name,o.salary,o.language)