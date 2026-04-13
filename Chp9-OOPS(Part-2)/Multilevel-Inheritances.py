class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car Stop")

class toyoto(Car):
    def __init__(self,brand):
        self.brand = brand

class fortuner(toyoto):
    def __init__(self,type):
        self.type = type

c1 = fortuner("Disel")
print(c1.start())