units=int(input("enter the units:"))
bill=0

if units<=100:
    bill=units*1.50

elif units<=200:
    bill=(100*1.50)+((units-100)*2.50)
elif units>200:
    bill=(100*1.50)+(100*2,50)+((units-200)*400)

    print("bill is ${bill}")    