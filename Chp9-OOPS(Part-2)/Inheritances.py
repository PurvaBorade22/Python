class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car Start...")

    @staticmethod
    def stop():
        print("Car Stop...")

class toyoto(Car):
    def __init__(self,name):
        self.name = name

car1 = toyoto("Fortune")
car2 = toyoto("BMW")

print(car1.color)
