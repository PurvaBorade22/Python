class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img,"j")

    def __add__(self,num2):   #self is 1st number #dunder function
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)

num1 = Complex(2,4)
num1.showNumber()

num2 = Complex(5,6)
num2.showNumber()

num3 = num1 - num2 #it work bcoz of __add__ this method
num3.showNumber()