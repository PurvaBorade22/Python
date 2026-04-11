#Example 1
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass   #private attribute (__)

#     def reset_pass(self):
#         print(self.__acc_pass)

# c1 = Account("abc","abc@123")
# print(c1.acc_no)
# print(c1.reset_pass())

#Example 2

class Person:
    __name = "anonymous"

    def __hello(self):
        print("Hello Person")

    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())
