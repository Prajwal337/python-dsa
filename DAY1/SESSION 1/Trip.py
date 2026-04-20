distance=int(input("enter distance in km:"))
milage=int(input("enter milage per ltr :"))
fuel_price=int(input("enter price per ltr:"))
Toll_charge=int(input("enter toll:"))
daily_wages=int(input("enter wages:"))
budget=int(input("enter budget:"))
num_of_days= distance//500

Fuel_cost = (distance / milage) * fuel_price
Driver_cost = daily_wages*num_of_days
Totaltripcost = Fuel_cost + Toll_charge + Driver_cost

if Totaltripcost > budget:
    print("OVER BUDGET by ", (Totaltripcost-budget))
else:
     print("WITHINBUDGET, savings =",(budget-Totaltripcost)) 