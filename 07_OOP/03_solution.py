# Parent class
class Car:
    def __init__(self, brand, model):
        # Initialize brand and model of the car
        self.brand = brand
        self.model = model

    def display(self):
        # Display car information
        print("Brand:", self.brand)
        print("Model:", self.model)


# Child class (Inheritance)
class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        # Call the constructor of the parent class
        super().__init__(brand, model)

        # Initialize battery size for the electric car
        self.battery_size = battery_size


# Create an object of Electric_Car class
new_electric_car = Electric_Car("Tesla", "M-29", "45")
