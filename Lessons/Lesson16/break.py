#Write a program to check alphabet “A” is present in the given string or not. 
#And terminate the loop after finding the alphabet “A.”
a= input("Enter a sentence")
for i in a:
    if i=='A' or i=='a':
        print("Found")
        break
    else:
        print("Not found")    