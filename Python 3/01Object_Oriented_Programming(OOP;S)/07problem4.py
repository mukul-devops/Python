class Calculator:
    def __init__(self,n):
        self.n = n
    @staticmethod
    def greet():
        print("hello")
    def square(self):
        print(f"Square of the no {self.n*self.n}")    
    def cube(self):
        print(f"Square of the no {self.n*self.n*self.n}")    
    def cuberoot(self):
        print(f"Square of the no {self.n**1/2}")    

      

n = Calculator(4) 
n.greet()
n.square()
n.cube()
n.cuberoot()

        