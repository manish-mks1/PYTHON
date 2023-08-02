# creating a dictionary for SIIET 
college = { "name": "siiet",
            "code": "INDI",
            "id": "x3"
        }
print(college)
#adding items to dictionary 
college["location"] = "IBP" 
print(college)
#changing values of a key 
college["location"] = "sheriguda" 
print(college)
# to remove items use pop() 
college.pop("code") 
print(college)
#know the length using len() 
print("length of college is:",len(college)) 
#to copy the same dictionary use copy() 
mycollege= college.copy() 
print(mycollege)
