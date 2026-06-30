print("It is a Pattern of Floyd Triangle")
n= int(input("Enter a Number: "))
a=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a ,end=" ")
        a=a+1
    print()       
