class Engine:
    def engine_info(self):
        print("Engine type: Petrol")

class Body:
    def body_info(self):
        print("Body type: Sedan")
    def engine_info(self):
        print("Engine type new : Diesel")

class Car(Engine, Body):  # inherits both
    def car_info(self):
        print("This is a car")

# usage
c = Car()
c.engine_info()  # from Engine
c.body_info()    # from Body
Body.engine_info(c) # calling engine info from body class
c.car_info()     # from Car
