def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b    
try:
    print("Welcome! to the Function Calculator.")    
    print("Press 1 for Addition.")
    print("Press 2 for Subtraction.")
    print("Press 3 for Multiplication.")
    print("Press 4 for Division.")
    choice= int(input("Enter your Choice: "))
    a= float(input("Enter a number"))    
    b= float(input("Enter a number"))
    if choice==1:
        print("The Sum of the Numbers is " ,add(a,b))
    elif choice==2:
        print("The Difference of the Numbers is " ,subtract(a,b))
    elif choice==3:
        print("The Product of the Numbers is " ,multiply(a,b))
    elif choice==4:
        print("The Quotient of the Numbers is " ,divide(a,b))            
    else:
        print("Invalid Choice.")
except ZeroDivisionError :
    print("There is Zero Division Error.")        
except ValueError:
    print("There is a Value Error.")
except:
    print("There is some Exception.")    

