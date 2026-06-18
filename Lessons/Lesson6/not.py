# 1) Store values in `a`, `b`, and `c`.
# 2) Check if `a` is not equal to `b` using `!=` and print the result (True/False).
# 3) Check if `b` is not equal to `c` using `!=` and print the result (True/False).
# 4) Store two strings in `a` and `b`.
# 5) If `a` is not equal to `b`, print a message saying they are different.
# 6) Store new numeric values in `a` and `b`.
# 7) Check this condition: (a equals 1) is not the same as (b equals 5).
# - If exactly one of these comparisons is True, the condition becomes True.
# - If the condition is True, print "Hello".
# 8) Take an integer input from the user and store it in `a`.
# 9) Check if `a` is not divisible by 2 (remainder is not 0).
# - If true, print that `a` is not an even number (it is odd).
a= 10
b= 4
c= -5
if a!=b :
    print("True")
else:
    print("False") 
print(b!=c)
a= "Hello" 
b= "World"
if a!=b :
    print("Strings are different")
else:
    print("Strings are same")  
a= 10
b= 15
if (a==1)!=(b==5):
    print("Hello")   
a= int(input("Enter a number"))    
if (a%2)!=0:
    print("the number is odd")
else:
    print("the number is even")    