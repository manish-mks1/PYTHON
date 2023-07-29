evenlist =[]
oddlist =[]
print("Enter first Range:",end="")
n=int(input())
print("Enter last range:",end="")
m=int(input())
if(n>m):
    n=n+m
    m=n-m
    n=n-m
for i in range(n,m+1):
    if(i%2==0):
         evenlist.append(i)
    else:
        oddlist.append(i)
print("Odd number:",oddlist)
print("Even number:",evenlist)
