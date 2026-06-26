#sum of natural numbers
num= int(input("Enter a number"))
sum=0
x=1
#for x in range(1,num+1):
#    sum= sum+x
#    print(sum)    
#print("The final sum is " ,sum)
while x<=num:
    sum= sum+x
    x+=1
print(sum)