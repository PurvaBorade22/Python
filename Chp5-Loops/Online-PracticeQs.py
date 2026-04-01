# for i in range(1,10):
#     print('*' * i)


# for i in range(5,0,-1):
#     print('*' * i)

# n=4
# for i in range (1, n+1):
#     print(" " * (n-i)+ "*" * (2*i-1)) 


#Print sum of first n numbers
# n = 7
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("Sum of all number is:", sum)

#Print sum of even numbers between 1 to n
# n = 10
# sum = 0
# for i in range(2, n+1, 2):
#     sum += i
# print("sum of all even numbers is:",sum)

#Print factorial of a number
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print("factorial of:",fact)

#Print numbers from 1–50:
# If divisible by 3 → print "Fizz"
# If divisible by 5 → print "Buzz"
# If both → print "FizzBuzz"

#Q4 divisiblity of 3 & 5
# n = 50
# for i in range(1,n+1):
#     if (i%3 ==0 and i%5 ==0):
#         print("FizzBuzz")
#     elif(i%3  == 0):
#         print("Fizz3")
#     elif(i%5 == 0):
#         print("Buzz5")
#     else:
#         print(i)

#count how many even and odd 
n= 50
even_count = 0
odd_count = 0
for i in range(1,n+1):
    if i%2 == 0:
        even_count +=1
    else:
        odd_count += 1
print("Count of even numbers is:", even_count)
print("Count of odd number is:",odd_count)