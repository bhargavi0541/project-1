english= int(input("Enter english marks:"))
maths= int(input("Enter maths marks: "))
hindi= int(input("Enter hindi marks: "))
science= int(input("Enter science marks: "))
history= int(input("Enter history marks: "))
average= (english+maths+hindi+science+history)/5
if average in range(91,100):
    print("Grade A1")
elif average in range(81,90):
    print("Grade A")     
elif average>=70:
    print("Grade B1")    
else:
    print("work harder.")    