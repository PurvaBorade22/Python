marks = int(input("Enter Student Marks : "))

if(marks>= 90):
    grade ="A"
elif(marks>=80 and marks<90): #marks between 80-90
    grade ="B"
elif(marks>=70 and marks<80): #marks between 80-70
    grade= "C"
else:
    grade ="D"
print("grade of the student-> ",grade)