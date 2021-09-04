class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display(self):
        output_maker = "I'm a " + self.make
        output_model = f"My model is {self.model}"
        print(output_maker)
        print(output_model)


if __name__ == "__main__":
    car1 = Car("Honda", "Civic")
    car1.display()

    car2 = Car("Toyota", "Prius")
    car2.display()
