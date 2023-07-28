num=int(input("Enter a number :"))
temp=num
sum,t=0,0
while(temp!=0):
    t=temp%10
    temp=temp//10
    sum =sum + (t**3)
if(num==sum):
   print("Your ",num," is an Armstrong numeber")
else:
   print("Your ",num," is not an Armstrong numeber")
