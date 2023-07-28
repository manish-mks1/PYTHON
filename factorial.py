print("**** To find factorial *****")
n=int(input("Enter a number for calculate factorial: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print("factorial :",fact)
