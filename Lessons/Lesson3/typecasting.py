# Create variables to store different types of values:
# - `name` as text (string)
# - `age` as a whole number (integer)
# - `is_student` as True/False (boolean)
# - `weight` as a decimal number (float)
# 2) Print each variable’s value.
# 3) Print the datatype of each variable using `type()`.
# 4) Show a message that type casting will happen next.
# 5) Convert `age` from an integer to a string and store it back in `age`.
# 6) Print `age` and print its datatype again to confirm it changed.
# 7) Convert `weight` from a float to an integer and store it back in `weight`.
# 8) Print `weight` and print its datatype again to confirm it changed.
name= "Bhargavi"
age= 16
is_student= True
weight= 52.1
print(f"the name is {name} and the age is {age} {is_student} is a student and the weight is {weight} ")
print("the datatype of name is:" ,type(name))
print("the datatype of age is:" ,type(age))
print("the datatype of is_student is:" ,type(is_student))
print("the datatype of weight is:" ,type(weight))
print("Now typecasting is happening,")
age= str(age)
print("the changed datatype of age is:" ,type(age))
weight= int(weight)
print("the value and changed datatype of weight is" ,weight ,type(weight))