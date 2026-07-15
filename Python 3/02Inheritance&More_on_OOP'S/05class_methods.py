class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"this shows the class attributes is {cls.a}")

e = Employee()
e.a = 34
e.show()