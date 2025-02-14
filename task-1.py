class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print(f"Car Details:\n"
              f"Make: {self.make}\n"
              f"Model: {self.model}\n"
              f"Year: {self.year}\n"
              f"Color: {self.color}\n")

car1 = Car("Ford", "Ranger", 2013, "Blue")
car2 = Car("Honda", "Civic", 2010, "White")

car1.display_info()
car2.display_info()