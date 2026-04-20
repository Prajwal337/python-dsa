name=input("enter name:")
quantity=int(input("enter quantityr:"))
unit=float(input("enter the price:"))
member=bool(input("member or not:"))

Subtotal = quantity * unit
discount = 0
if member == 1:
     discount=Subtotal*0.10
discounted_amt=Subtotal-discount

if discounted_amt>500:
    gst=Subtotal*0.05
else:
    gst=Subtotal*0.12

Finaltotal =Subtotal-discount+gst
print(Finaltotal)