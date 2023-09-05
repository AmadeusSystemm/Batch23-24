a=eval(input("Enter the total shopping Amount-"))
pa=0.2*a
pb=0.1*a
pc=0.05*a
if a>25000:
    print("The Amount to be paid",a-pa)
elif 25000>a>10000:
    print("The Amount to be paid",a-pb)
else:
    print("The Amount to be paid",a-pc)

