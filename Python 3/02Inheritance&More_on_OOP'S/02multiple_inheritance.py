class Employee:
    company = "ITC"
    name = "Default name"
    language = "c"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "java"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")
     


class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()  #in this case (like parent1 class have language = c and parent2 class have language = python )
                  #it prefers parent1 class's attributes(like it shows langauge = c) 