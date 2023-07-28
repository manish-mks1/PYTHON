p = float(input(("Enter Principle amount: ")))
t = float(input(("Enter Time: ")))
r = float(input(("Enter Rate: ")))
Ci = p*pow(t,(1+r/100))-p
Si = (p * t * r) / 100
print("CI is: ", round(Ci,2))
print("SI is: ", round(Si,2))