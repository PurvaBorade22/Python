#Q1 length of a list
cities = ["Mumbai","Pune","Airoli","Navi Mumbai","Thane","Mulund","CSMT"]

def get_len(city_list):
    print("length of cities is:",len(city_list))
    return city_list
get_len(cities)

#Print list item in a single line (hint: "end function of print()")
cities = ["Mumbai","Pune","Airoli","Navi Mumbai","Thane","Mulund","CSMT"]
 
def print_list(list):
    for item in list:
        print(item, end=" ")