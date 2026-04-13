class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stop...")

class Toyoto(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        super().start()   #this line print car start 

c1 = Toyoto("prius", "electric")
print(c1.type)