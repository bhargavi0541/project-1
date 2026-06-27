lower= int(input("Enter a low number"))
higher= int(input("Enter a higher number"))
prime=0
for x in range(lower,higher+1):
    count=0
    for y in range(2,x):
        if x%y==0:
            break
    else:
         prime= prime+1
         print("The prime numbers are " ,x)
print("\n The number of prime number is " ,prime)
