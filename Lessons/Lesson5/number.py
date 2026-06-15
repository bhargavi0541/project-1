#to check whether a number is greater than or smaller than 15
num= input("Enter the number")
print(num)
print(type(num))
number= int(num)
print(type(number))
if number>15:
    print("number is greater than 15")
elif number<15:
    print("number is less than 15")    
else:
    print("the number is 15")    