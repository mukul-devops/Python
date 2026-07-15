class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")





class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
a.name = "Karan"
a.language = "English"
a.salary = "1200000"
a.show()


b = Programmer()
b.name = "Mukul"
b.language = "python"
b.salary = "1200000"
print(a.company, b.company)
b.showLanguage()
b.show()