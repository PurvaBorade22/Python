class Student:
    def __init__(self,fullname,age):
        self.name = fullname
        self.age = age
        print("Adding another student...")

s1 = Student("Purva",22)
print(s1.name)
print(s1.age)
