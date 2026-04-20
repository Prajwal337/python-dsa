bal = 100000
type = int(input("enter type of account:\n 1 Savings\n 2 Current"))
amt = int(input("Enter Amt to withdraw"))
if(type == 1):
    if(amt > 50000):
        print("Max limit")
    elif(amt > (bal-500)):
        print("Insufficient balence..!")
    else:
        bal -= amt
        print("Transaction succsfull")
        print("Current balence is: ",bal)
elif(type == 2):
    if(amt > bal):
        print("Insufficient balence..!")
    elif(amt > 25000):
        bal -= (amt+50)
    else:
        bal -= amt
    print("Transaction succsfull")
    print("Current balence is: ",bal)

else:
    print("Enter proper account type")