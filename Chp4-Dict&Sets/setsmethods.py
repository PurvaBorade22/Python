collection = set()
collection.add(1) #add an element
collection.add(2)
collection.add(3)
collection.add("Hello")
collection.add((1,3,4))

collection.remove(3) #remove an element

collection.clear() #clear the set 

print(len(collection))

collection2 = {"Python", "Hello", "Krutika", "Aditya"}
print(collection2.pop()) #print any element from the list noy fixed element

set1 ={1,2, 3}
set2={2,3,4,5}

print(set1.union(set2)) #combine both set values

print(set1.intersection(set2)) #return common value from both the sets

