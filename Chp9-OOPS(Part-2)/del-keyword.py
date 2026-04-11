class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Purva")
print(s1.name)   #first print
del s1.name      #then delete
print(s1.name)   #agian print