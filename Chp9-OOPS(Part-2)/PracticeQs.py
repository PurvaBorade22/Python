#Q1
# class Circle:
#     pie = 3.14
#     def __init__(self,radius):
#         self.radius = radius

#     @property
#     def Area(self):
#         return self.pie * self.radius *self.radius

#     @property
#     def perimeter(self):
#         return 2 * self.pie * self.radius
    
# circle1 = Circle(5.8)
# print("Area is: ", circle1.Area)
# print("Perimeter is:", circle1.perimeter)


#Q2
# class Employee:
#     def __init__(self,role,dep,sal):
#         self.role = role
#         self.dep = dep
#         self.sal = sal

#     def showDetails(self):
#         print("Role:", self.role)
#         print("Department:", self.dep)
#         print("Salary:", self.sal)
        
# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         super().__init__("Software Tester","IT", "60,000")

# emp1 = Engineer("Purva",22)
# emp1.showDetails()


#Q3
class Order:
    def __init__(self, item,price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
        return self.price > odr2.price

odr1 = Order("pizza",200)
odr2 = Order("Burger",100)

print(odr1 > odr2)

