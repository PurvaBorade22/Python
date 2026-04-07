#Reading a file
# f = open("D:\PURVA\Python\Python\Chp7-File_Input&Output\demo.txt","r")
# data = f.read()
# print(data)

# line2 = f.readline()
# print(line2)

# f.close()


#Writing to a file
# f = open("D:\PURVA\Python\Python\Chp7-File_Input&Output\demo.txt","a")
# f.write("\nThis is another line")
# f.close()

#Create new file directly
# f = open("sample.txt","w")
# f.close()

#R+ mode ->overwrite

f = open("D:\PURVA\Python\Python\Chp7-File_Input&Output\demo.txt","r+")
f.write("abc")
print(f.read())
f.close()