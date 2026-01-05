# Define a class named Car
class Car:
    def __init__(self, brand, model):
        # Initialize brand and model attributes
        self.brand = brand
        self.model = model

    def display(self):
        # Display the car's details
        print("Model :", self.model)
        print("Brand :", self.brand)


# Create an object of the Car class
my_car = Car("Tesla", "X-ito")

# Call the display method to show car information
my_car.display()
