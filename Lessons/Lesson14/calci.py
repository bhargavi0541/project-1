# 1) Define a function `add(P, Q)` that returns the sum of two numbers (P + Q).
# 2) Define a function `subtract(P, Q)` that returns the difference of two numbers (P - Q).
# 3) Define a function `multiply(P, Q)` that returns the product of two numbers (P * Q).
# 4) Define a function `divide(P, Q)` that returns the division result of two numbers (P / Q).
# 5) Display a menu to the user showing the available operations:
# a) Add
# b) Subtract
# c) Multiply
# d) Divide
# 6) Take the user's choice as input and store it in `choice`.
# 7) Take two integer inputs from the user:
# a) Store the first number in `num_1`
# b) Store the second number in `num_2`
# 8) Use conditional statements to perform the chosen operation:
# a) If `choice` is 'a', call `add(num_1, num_2)` and print the result.
# b) Else if `choice` is 'b', call `subtract(num_1, num_2)` and print the result.
# c) Else if `choice` is 'c', call `multiply(num_1, num_2)` and print the result.
# d) Else if `choice` is 'd', call `divide(num_1, num_2)` and print the result.
# 9) If the user enters anything other than a/b/c/d, print an invalid input message.
def add(p,q):
    print(p+q)
def subtract(p,q):
    print(p-q)
def multiply(p,q):
    print(p*q)
def divide(p,q):
    print(p/q)  
p= int(input("Enter a number1 "))    
q= int(input("Enter a number2 "))  
choice= input("Enter a for addition, b for subtraction, c for multiplication, d for division")  
if choice=='a':
    add(p,q)
elif choice=='b':
    subtract(p,q)
elif choice=='c':
    multiply(p,q)
elif choice=='d':
    divide(p,q)
else:
    print("invalid choice")    

