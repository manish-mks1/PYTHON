dict1={'apple':'fruits','age':23,'address':'noida'}
z=1
while(z!=0):
    flag=0
    print("**Dictionary***")
    print("1. Search Word meaning")
    print("2. Add word meaning")
    print("Enter your choice:",end=" ")
    n=int(input())
    if n==1:
        t= input("Type a word for search: ")
        for x in dict1:
            if x==t:
                print(x," = ",dict1[x])
                print("Thank You...")
                flag=1
        if(flag==0):
            print("your word are not found")
            print("please add this word to dictionary...")
            print("Thank you...")
    elif n==2:
        print("******* Add word with meaning in dictionary **********")
        print("Please Enter word with meaning by space seperated:",end=" ")
        values=input()
        list=values.split(" ")
        dict1[list[0]]=list[1]
        print("your word is add successfully...")
    else:
        print("invalid input")
        print("please try again")
    print("Do you want to continue y/n :",end=" ")
    x=input()
    if x=='n' or x=='N':
        print("Thanks for Visiting my dictionary...")
        z=0