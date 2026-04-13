class Person:
    name = "annoymous"

    # def changename(self,name):
    #     Person.name = name #class method

    @classmethod
    def changename(cls,name):
        cls.name = name

p1 = Person()
p1.changename("Purva Borade")
print(p1.name)
print(Person.name)