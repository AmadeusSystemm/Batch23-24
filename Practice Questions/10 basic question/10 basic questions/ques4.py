a=int(input("enter user's age "))
x=  a >= 18
print(x)
print("user is eligible to vote"*x + "user is ineligible to vote"*(1-x))