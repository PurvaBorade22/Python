with open("D:\PURVA\Python\Python\Chp7-File_Input&Output\demo.txt","r") as f:
    data = f.read()
    print(data)

with open("D:\PURVA\Python\Python\Chp7-File_Input&Output\demo.txt","w") as f:
    f.write("This is new line")

    