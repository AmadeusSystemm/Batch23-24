p=eval(input("Intial principal balance "))
r=eval(input("Interest rate "))
n=eval(input("Number of times interest applied per time period "))
t=eval(input("Number of time period Elapsed "))
a=p*(1+r/n)**n*t
print("the given total amound is ",a)