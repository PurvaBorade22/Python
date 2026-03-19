Student = {
    "name" : "Purva",
    "Age": 22,
    "Subjects" : {
        "python" : 90,
        "Eng" : 80,
        "Maths" : 70
    }
}
print(list(Student.keys())) #return all keys in the list

print(list(Student.values())) #return all the values in the list

print(Student.items()) # return all keys, value as a tuple

print(Student.get("name")) #return value according to key

Student.update({"city": "Airoli"}) #update the dictionary
print(Student)