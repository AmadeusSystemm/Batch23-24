import math
a=int(input("enter side1-"))
b=int(input("enter side2-"))
c=int(input("enter side3-"))
s=a+b+c/2
s1=math.sqrt(s*(s-1)*(s-2)*(s-3))
print(s1)