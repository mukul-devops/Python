class Programmers:
    company = "Mcrosoft"
    def __init__(self, name, salary, pin ):
        self.name = name
        self.pin = pin
        self.salary = salary
    
m = Programmers("Mukul",1200000,124103)
print(m.name,m.salary,m.pin,m.company)        
k = Programmers("Karan",1200000,124103)
print(k.name,k.salary,k.pin,k.company)        

