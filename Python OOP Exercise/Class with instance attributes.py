class Vehicle:
    def __init__(self, max_speed, mileage) -> None:
        self.max_speed = max_speed
        self.mileage = mileage

car1 = Vehicle(200, 10)
print(f"Max speed: {car1.max_speed}\nMileage: {car1.mileage}")