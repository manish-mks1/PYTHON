colleges = ["GU", "GNIT", "AMITY"]

print(colleges)

# appending new college in collges list

colleges.append("GLBajaj") #checking if its added or not 
print(colleges)

#adding a new college at a positon 
colleges.insert(1,"BHARAT") 
print(colleges) 

#remove a name from colleges 
colleges.remove("BHARAT") 
print(colleges)

#remove a name with an index value
del colleges[1]

# NOTE: index starts from 0 so 2nd value in list will be removed

print(colleges)
