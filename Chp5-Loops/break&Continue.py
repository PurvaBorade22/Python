#brak statement basic code
#1
i = 1
while i <= 5:
    print(i)
    if (i == 3):
        break 
    i += 1 

##2
numbers = (1,4,9,16,36,49,64,81,100,36,36)
x = 36
i= 0
while i < len(numbers):
    if(numbers[i] == x):
        print("found at idx:", i)
        break
    else:
        print("founding.....")
    i += 1