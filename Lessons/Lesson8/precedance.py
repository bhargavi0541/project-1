# 1) Store values in `v`, `w`, `x`, `y`, and `z`.
# 2) Calculate the expression (v + w) * x / y and store the result back in `z`.
# 3) Print the value of `z` with a message.
# 4) Store a name in `name` and a number in `age`.
# 5) Check this condition using `or` and `and`:
# - The code checks if `name` is "Alex"
# OR (if `name` is "John" AND `age` is 2 or more).
# - If the condition is true, print the welcome message.
# - Otherwise, print the goodbye message.
v=10
w=5
x=2
y=3
z=1
z= (v + w) * x / y
print(f"The calculated expression is: {z}")
name= input("Enter your name:")
age= int(input("Enter your age"))
if name=="Alex" or name=="John" and age>=2:
    print(f"Welcome {name}")   
else:
    print(f"Goodbye {name}")    