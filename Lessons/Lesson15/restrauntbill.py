def restrauntbill(bill,percentage):
    final= bill-(percentage/100)*bill
    return final
bill= float(input("Enter bill amount."))  
percentage= int(input("Enter rate of discount."))  
print(restrauntbill(bill,percentage))    