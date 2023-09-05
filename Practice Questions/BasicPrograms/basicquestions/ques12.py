a=int(input("Enter the first side of the triangle "))
b=int(input("Enter the second side of the triangle "))
c=int(input("Enter the third side of the triangle "))
x=a!=b & b!=c & c!=a
y=(a==b) | (b==c) | (c==a)
z=c**2==a**2+b**2
print("scalene "*x + "isosceles "*y + "rightangled "*z )
"""solution is only valid given c is the biggest side """