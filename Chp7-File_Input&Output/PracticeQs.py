#Q1
# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning file I/O\n")
#     f.write("using Java\nI like programming in Java")

#Q2 overwrite java with python
# with open("practice.txt","r") as f:
#     data = f.read()

# new_data= data.replace("java","Python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)


#Q3
# def check_for_word():
#     word = "learning"
#     with open("practice.txt","r") as f:
#         data = f.read()
#     if (data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not found")
    
# check_for_word()

#Q4
# def check_for_line():
#     word = "like"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
    
#     return -1
# check_for_line()



#Q5 find count of even numbers using split method
even_count = 0
with open("practice.txt","r") as f:
    data = f.read()

    num = data.split(",")
    for val in num:
        if(int(val) %2 == 0):
            even_count += 1

print(even_count)   