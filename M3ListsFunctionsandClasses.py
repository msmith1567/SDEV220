# Author: Max Smith
# Date: 2024-11-10

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Define the Automobile subclass, inheriting from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        # Display information in a readable format
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

# App logic to accept user input and display the car's information
def main():
    # Vehicle type is always "car" for this app
    vehicle_type = "car"
    
    # Collect car details from the user
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")
    
    # Create an Automobile object with the collected information
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    
    # Display the information
    print("\nCar Information:")
    car.display_info()

# Run the app
if __name__ == "__main__":
    main()