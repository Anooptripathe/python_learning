class vehicle:

    def __init__(self,brand):
        self.brand=brand

    def start(self):
        print(f"{self.brand} vehicle started.")

class car(vehicle):
    def drive(self):
        print(f"{self.brand} is being driven")

c=car("Tata")
c.start()
c.drive()

    
    
