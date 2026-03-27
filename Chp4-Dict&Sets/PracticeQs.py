## Q1
dic = {
    "table" : ["a pieces of furniture", "list of facts and figure"], 
    "cat" : "a small animal"
}
print(dic)


##Q2
subjects = {
    "python", "java", "C++", "python", "javascript", "java", "python" ,"java", "C++", "C"
}
print(subjects)
print("The classrooms will be needed for every subject is :", len(subjects))


##Q3
dictionary ={}

x = int(input("Enter marks for phy: "))
dictionary.update({"phy": x})

y = int(input("Enter marks for chem: "))
dictionary.update({"chem": y})

z = int(input("Enter marks for eng: "))
dictionary.update({"eng": z})

print(dictionary)


##Q4
set = {9, "9.0"}
print(set)