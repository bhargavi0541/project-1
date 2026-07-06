num1= int(input("Enter a number"))
try:
    num1/0
    raise ZeroDivisionError
except:
    print("There is an exception")    