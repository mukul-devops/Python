class TwoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The 2D vector is {self.i}i+{self.j}j")

class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The 3d vector is {self.i}i+{self.j}j+{self.k}k")

o = TwoDvector(3,4)
e = ThreeDvector(1,2,5)
o.show()
e.show()