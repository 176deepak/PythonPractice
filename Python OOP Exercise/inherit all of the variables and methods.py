class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

bus_obj = Bus("TATA", 180, 15)

print(f"Vehicle Name: {bus_obj.name} Speed: {bus_obj.max_speed} Mileage: {bus_obj.mileage}")