num= int(input("Enter a number"))
og=num
pow= len(str(num))
sum=0
while num>0:
    sum= sum+ (num%10)**pow
    num= num//10
if og==sum:
    print("Armstrong Number")    
else:
    print("Not Armstrong Number")    
print(sum)    