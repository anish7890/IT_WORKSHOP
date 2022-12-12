
a=float(input("ENTER THE FIRST SIDE"))
b=float(input("ENTER THE SECOND SIDE"))
c=float(input("ENTER THE THIRD SIDE"))

s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("AREA OF TRIANGLE is %.2f" %area)