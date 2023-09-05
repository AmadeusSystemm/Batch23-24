a=eval(input("enter the time in seconds "))
h=a//60
h1=h//60
a=a-(h1*60*60)
m=a//60
a=a-(m*60)
print(h1,m,a)        