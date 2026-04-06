#Q1
def cal_sum(n):
    if (n == 0):
        return 0
    return cal_sum(n-1) + n

sum = cal_sum(5)
print(sum)


#Q2 print list

def ele_list(list,idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    ele_list(list,idx+1)

fruits = ["apple","banana","grapes","Orange"]
ele_list(fruits)


