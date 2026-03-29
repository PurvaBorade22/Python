Q1
list = [1,4,9,16,36,49,64,81,100]
for val in list:
    print(val)


#Q2 find number (normal method)
list2 = [1,4,9,16,36,49,64,81,100]
x = 64
for val in list2:
    if(x == val):
        print("Number found", x)
        break
    print(val)
else:
    print("Not found")

#2.1 found number using index method

list2 = [1,4,9,16,36,49,64,81,100,16,77,16]
x = 16
idx = 0
for el in list2:
    if (el == x):
        print("Found at index: ", idx)
    idx += 1
