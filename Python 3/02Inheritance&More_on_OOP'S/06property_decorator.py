class Employee:
    @property
    def name(self):
        return self.ename

e = Employee()
e.ename = "mukul"
print(e.name)   # no brackets needed
