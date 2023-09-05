import math
r=eval(input("Enter the Radius-"))
p,q = input("Enter Arbitrary Constant X and Y-").split()
x=int(p)
y=int(q)
dist=math.sqrt(x**2 + y**2)
if r>dist:
    print("Point lies inside the circle")
elif dist>r:
    print("Point is outside the circle")
else:
    print("point is on the radius of curvature")

