class Animal:
    @staticmethod
    def __init__():
        print("this is a class of animal ")
class Pet(Animal):
    @staticmethod
    def __init__():
        print("this is a class of pet ")

class Dog(Pet):

    def __init__(self,dog):
        self.dog = dog
        super().__init__()
        print("this is a class of dog ")
    def method(self):

        print(f"{self.dog} barks")

# a = Animal()
# b = Pet()
c = Dog("jack")
c.method()
