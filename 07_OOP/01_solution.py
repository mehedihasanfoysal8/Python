# Define a class named Car
class Car:
    def __init__(self, brand, model):
        # Initialize brand and model attributes
        self.brand = brand
        self.model = model

# Create an object of the Car class
new_car = Car("Tesla", "X-ioy")

# Access and print object attributes
print(new_car.brand)
print(new_car.model)
