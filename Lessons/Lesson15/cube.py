#Define a function to find a cube 
#define another function which let execute the cube function if the number is divisible by 3
def cube(number):
    return number**3
def divisible(number):
    if number%3==0:
        print("YES DIVISIBLE" ,cube(number))
    else:
        print("NOT DIVISIBLE")        
number= int(input("Enter a number:"))        
divisible(number)