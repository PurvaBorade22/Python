#Q1 length of a list
# cities = ["Mumbai","Pune","Airoli","Navi Mumbai","Thane","Mulund","CSMT"]

# def get_len(city_list):
#     print("length of cities is:",len(city_list))
#     return city_list
# get_len(cities)

#Q2 Print list item in a single line (hint: "end function of print()")
# cities = ["Mumbai","Pune","Airoli","Navi Mumbai","Thane","Mulund","CSMT"]
 
# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(cities)

#Q3 find the factorial of n
# def fact_no(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#     return fact
# print(fact_no(3))   

#Q3 convert USD to inr
# def USD(rupee):
#     rate = 83
#     INR = rupee * rate
#     return INR

# result= (USD(3))
# print(result)

#Q4 odd and even
def odd_even(num):
    if num % 2 == 0:
        print(num,"Is even") 
    else:
        print(num,"Is odd")
    return num
odd_even(10)