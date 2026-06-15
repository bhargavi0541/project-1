# 1) Ask the user to enter marks for 4 subjects: math, english, science, and hindi.
# Store each mark in its own variable.
# 2) Add all 4 subject marks and store the total in `sum`.
# 3) Print the total marks stored in `sum`.
# 4) Calculate the percentage:
# - Divide `sum` by 400 (total maximum marks for 4 subjects, assuming each is out of 100)
# - Multiply the result by 100
# Store the final value in `perc`.
# 5) Print the percentage stored in `perc`.
math= int(input("enter maths marks"))
english=int(input("enter english marks"))
science=int(input("enter science marks"))
hindi=int(input("enter hindi marks"))
sum=math+english+science+hindi
print("the sum of all subjects:" ,sum)
perc=(sum/400)*100
print("the percentage is:" ,perc)
