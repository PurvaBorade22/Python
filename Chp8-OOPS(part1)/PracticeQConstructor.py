#3 subject marks and print their avg 

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "this is your avg score: ", sum/3)



s1 = Student("Purva",[22,45,67])
s1.average()

s1.name ="Upasana" 
s1.marks = [23,56,78]
s1.average()