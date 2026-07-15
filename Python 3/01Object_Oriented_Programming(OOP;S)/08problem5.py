from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo
    def book(self,fro,to):
        print(f"Ticket is booked in train no {self.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"Train {self.trainNo} is running on time") 
    def getFare(self,fare):
        print(f"Train fare is {fare}")  



t = Train(12344)
t.book("delhi","rewari")
t.getStatus()
t.getFare(randint(234,555))
