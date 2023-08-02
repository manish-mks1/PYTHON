def bigOf3(a,b,c): 
    if(a>b):
        if(a>c):
            print("a is greater than b and c") 
        else:
            print("c is greater than a and b") 
    elif(b>c):
        print("b is greater than a and c") 
    else:
        print("c is greater than a and b") 

txt= input("enter a,b,c values:") 
a,b,c= txt.split()
bigOf3(int(a),int(b),int(c)) #calling the function