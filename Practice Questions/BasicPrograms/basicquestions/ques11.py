a=int(input("the Amount to be withdrawn "))
a-=100
ab=a//2000
a=a-(2000*ab)
ac=a//500 
a=a-(500*ac)
ad=a//100
print("the Number of 2000 Notes are ",ab)    
print("the Number of 500 Notes are ",ac)    
print("the Number of 100 Notes are ",ad+1)    

