class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluth = False

    def start(self):
        self.acc = True
        self.cluth = True
        print("Car start...")

c1 = Car()
c1.start()