class vehicle:
    def __init__(self,brand,wheels):
        self.brand=brand
        self.wheels=wheels
    
    def show_info(self):
        print(f"{self.brand} has {self.wheels}")

# Derived class

class car(vehicle):
    def __init__(self, brand, wheels,fuel_type):
        super().__init__(brand, wheels)
        self.fuel_type=fuel_type

    def car_info(self):
        print(f"Car uses {self.fuel_type} fuels")

class electric_vehicle(car):
    def __init__(self, brand, wheels, fuel_type,battery_capacity):
        super().__init__(brand, wheels, fuel_type)
        self.battery_capacity=battery_capacity

    def battery_info(self):
        print(f"Car uses {self.battery_capacity}")


xuv=electric_vehicle("mahindra",4,"electric",80)
xuv.show_info()
xuv.car_info()
xuv.battery_info()