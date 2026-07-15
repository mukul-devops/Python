class Empoyee:
    salary = 234
    increment = 20 
    @property
    def salaryAfterincement(self):
        return self.salary+(self.salary*self.increment/100)
    @salaryAfterincement.setter
    def salaryAfterincement(self,salary):
        self.increment = ((salary/self.salary)-1)*100

e = Empoyee()
# print(e.salaryAfterincement)
e.salaryAfterincement = 280.8
print(e.increment)
    

