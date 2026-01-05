# Define a class named Car
class Car:
    def __init__(self, brand, model):
        # Private attributes
        self.__brand = brand
        self.__model = model

    # Getter method for brand
    def get_brand(self):
        return self.__brand + "!"  # Add exclamation when returning

    # Setter method for brand
    def set_brand(self, new_brand):
        self.__brand = new_brand  # Update the private brand

    # Getter method for model
    def get_model(self):
        return self.__model + "!"  # Add exclamation when returning

    # Setter method for model
    def set_model(self, new_model):
        self.__model = new_model  # Update the private model


# Create a Car object
my_car = Car("Foysal", "Nai re bhai")

# Access initial values
print(my_car.get_brand())  # Output: Foysal!
print(my_car.get_model())  # Output: Nai re bhai!

# Update values using setter methods
my_car.set_brand("Tesla")
my_car.set_model("X-ito")

# Access updated values
print(my_car.get_brand())  # Output: Tesla!
print(my_car.get_model())  # Output: X-ito!
