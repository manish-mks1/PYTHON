str1=input("Enter first String: ")
str2=input("Enter second String: ")
len1=len(str1)
len2=len(str2)
i=0
while i<len1 or i<len2:
    if i<len1:
        print(str1[i],end="")
    if i<len2:
        print(str2[i]) 
    i+=1