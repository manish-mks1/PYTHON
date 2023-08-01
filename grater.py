print("****** check greater number from given three number *****")
a=int(input("Enter first number: "))
b=int(input("Enter second number:"))
c=int(input("Enter third number: "))
if a>b and a> c:
    print(a," is greater than then ",b," and ",c)
elif b>a and b>c:
    print(b," is greater than then ",a," and ",c)
else:
    print(c," is greater than then ",a," and ",b)