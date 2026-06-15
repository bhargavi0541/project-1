#to check if a person is buying oranges at 100 rupees and later selling at 120 rupees. Find the loss
selling= float(input("Enter the Selling Price"))
buying= float(input("Enter the Cost Price"))
if selling>buying:
    print("the person has gained profit")
    profit= selling-buying
    print(profit)
elif selling<buying:
    print("the person has suffered loss")   
    loss= buying-selling
    print(loss)
else:
    print("Neither profit or Loss")     