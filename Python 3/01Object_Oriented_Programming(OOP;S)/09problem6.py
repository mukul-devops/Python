from random import randint

class Train:
    def __init__(slf,trainNo):     
        slf.trainNo = trainNo
    def book(harry,fro,to):
        print(f"Ticket is booked in train no {harry.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"Train {self.trainNo} is running on time") 
    def getFare(self,fare):
        print(f"Train fare is {fare}")  



t = Train(12344)
t.book("delhi","rewari")
t.getStatus()
t.getFare(randint(234,555))
# there is no change in anything by changing self to slf but readablity of code is diturb