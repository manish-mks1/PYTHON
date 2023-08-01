list1=[10,20,30,40,25,10,18]
list2=[5,50,20]
list3=list1+list2
print("length of list is ",len(list3))
print("adition of list is ",list3)
# print(10 in list3)
# n=int(input("Enter any number to search: "))
# if n in list3:
#     print("yes your data is present in database ")
# else:
#     print("your data is not present in database")
e=0
o=0
for i in list3:
    if i%2==0:
        e+=1
    else:
        o+=1
    i+=1
# while (i<=len(list3)):
#     if list3[i]%2==0:
#         e+=1
#     else:
#         o+=1
#     i+=1
print("number of even number is=",e," and number of odd is= ",o)