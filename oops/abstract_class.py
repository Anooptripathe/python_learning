from abc import ABC,abstractmethod

class computer(ABC): #to make a class abstract use ABC-> Abstract Base Class
    @abstractmethod  # to declare class in method use @abstract method
    def process(self):
        pass

class Laptop(computer):
    def process(self):
        print("Laptop needs to be upgraded")

l1=Laptop()
l1.process()