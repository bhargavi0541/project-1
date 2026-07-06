try:
    num1,num2= eval(input("Enter Two Numbers."))
    print(num1/num2)
except ZeroDivisionError:
    print("There is ZERO DIVISION ERROR. ")
except SyntaxError:
    print("There is a SYNTAX ERROR.")
except:
    print("There is an exception. ")            
else:
    print("no exception. ") 