class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def drive(self, number):
        self.mileage = self.mileage + number

blue_car = Car("blue", 20000)
red_car = Car("red", 30000)
yellow_car = Car("yellow", 0)

for car in (blue_car, red_car):
    print(f"The {car.color} car has {car.mileage} miles")

yellow_car.drive(100)
print(yellow_car.mileage)
