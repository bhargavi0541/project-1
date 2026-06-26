num= int(input("Enter a number;"))
og= num
k=0
while num>0:
    num= num//10
    k+=1
print("The number of digits is " ,k)