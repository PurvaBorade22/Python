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
# n= 50
# even_count = 0
# odd_count = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         even_count +=1
#     else:
#         odd_count += 1
# print("Count of even numbers is:", even_count)
# print("Count of odd number is:",odd_count)

#Count number of vowels in a string

# string =("Purva")
# vowels = ["a","e","i","o","u"]
# vowels_count = 0

# for ch in string:
#     if ch.lower() in vowels:
#         vowels_count += 1

# print("No. of vowels:",vowels_count)

#Reverse a string using loop

# string = input("Enter a string: ")
# reversed_string = ""

# for char in string:
#     reversed_string = char + reversed_string
# print("Reversed string is:",reversed_string)

#Check if string is palindrome

# list1 = [1,2,3]
# list1_copy =list1.copy()
# list1_copy.reverse()

# if list1_copy == list1:
#     print("List is palindrome")
# else:
#     print("List is not palindrome")

#Find sum of elements
# nums = [10, 20, 30, 40, 50]
# total = 0
# for num in nums:
#     total = total + num
# print("sum of all no.: ",total)

#Find max number
# nums = [10, 20, 30, 40, 50]
# max_num = nums[0]
# for num in nums:
#     if num > max_num:
#         max_num = num

# print("Max number is:",max_num)

#Count elements greater than 25
# nums = [10, 20, 30, 40, 50]
# num_count = 0
# for number in nums:
#     if number > 25:
#         num_count += 1

# print("Count is: ", num_count)

#Remove duplicates from list
#method 1
# list = [10, 20, 30, 40, 50, 10,30,40,50,30]
# new_list= []
# for num in list:
#     if num not in new_list:
#         new_list.append(num)
# print("New list is: ", new_list)

#method 2
# num = [10, 20, 30, 40, 50, 10,30,40,50,30]
# new_list= list(set(num))
# print(new_list)

#Print only valid URLs (hint: check "." in url)
urls = ["google.com", "test.com", "invalid", "purva.com", "college.edu", "borade","hello"]
for url in urls:
    if "." in url:
        print("valid url is:", url)
    # else:
    #     print("invalid urls: ",url)
    