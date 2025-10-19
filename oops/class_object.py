class car:
    wheels=4

    def __init__(self,power,average):
        self.power=power
        self.average=average
    def config(self):
        print(f"{self.power} cc with {self.average} avg in petrol version")
    def compare(self,car2):
        if self.power==car2.power:
            return True
        else:
            return False
    

c1=car(1350,22)
c2=car(1500,18)
print(type(c1))

car.config(c1)


c2.config()

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")