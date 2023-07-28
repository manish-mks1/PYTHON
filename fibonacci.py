print("\n**** print fibonccin series ****")
n=int(input("Enter number of terms: "))
i=1
a=0
b=1
if n<=0:
    print("Plese enter positive number\n")
else:
    print("Your",n," term fibonacci series is: ")
    while(i<=n):
        print(a,end=", ")
        t=a+b
        a=b
        b=t
        i+=1
