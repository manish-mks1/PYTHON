email =input("Enter email Id: ")
k,l,m=0,0,0
if len(email) >6:
    if email[0].isalpha():
        if ((email[-3]=='.') ^ (email[-4]=='.')):
            if ('@' in email and email.count('@')==1):
                for i in email:
                    if i==" ":
                        k=1
                    elif i.isalpha():
                        if i.isupper():
                            l=1
                        else:
                            continue
                    elif i.isdigit():
                        continue
                    elif i=='@' or i=='_' or i=='.':
                        continue
                    else:
                        m=1
                if k==1 or l==1 or m==1:
                    print("Invalid email 5")
                else:
                    print("Correct email")
            else:
                print("invalid input 4")
        else:
            print("plese valid email 3")
    else:
        print("enter valid email 2")
else:
    print("envalid email 1 ")
input()