p=eval(input("enter the principle amount "))
r=eval(input("enter the rate of interest "))
t=eval(input("enter the time period "))
si=p*r*t/100
total = p + si
print("the simple interest is ",si,"and the total amount is",total)