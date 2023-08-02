while(1):
    print("1.CELSIUS TO FAHRENHEIT\n2.FAHRENHEIT TO CELSIUS\n3.EXIT\n")
    choice=input("ENTER YOUR CHOICE:") 
    ch=int(choice)
    if(ch==1):
        c=int(input("ENTER TEMPERATURE IN CELSIUS:")) 
        f=((9*c)/5)+32
        print("converted temperature is:",f) 
    elif(ch==2):
        f=int(input("ENTER TEMPERATURE IN FAHRENHEIT:")) 
        c=((f-32)/9)*5
        print("converted temperature is:",c) 
    elif(ch==3):
        exit() 
    else:
        print("wrong choice")
