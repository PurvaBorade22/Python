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
def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("Not found")
    
check_for_word()
