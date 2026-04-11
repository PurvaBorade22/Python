class Student:
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks

    def welcome(self):
        print("Welcome student", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Purva",22)
s1.welcome()
print(s1.get_marks())