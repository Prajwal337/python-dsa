def calculate_ticket_price(day, time, age, seat_type):
    base_price = 200.0
    print(f"Base price: Rs {base_price:.2f}")
    current_price = base_price   
    if 1 <= day <= 4:
        discount = current_price * 0.20
        current_price -= discount
        print(f"Weekday discount (20%): -Rs {discount:.2f}")    
    if age < 12 or age > 60:
        age_discount = current_price * 0.30
        current_price -= age_discount
        print(f"Age discount (30%): -Rs {age_discount:.2f}")       
    surcharge = 0.0
    if seat_type == 2:
        surcharge = 100.0
        print(f"Seat surcharge (Premium): +Rs {surcharge:.2f}")
    elif seat_type == 3:
        surcharge = 250.0
        print(f"Seat surcharge (Recliner): +Rs {surcharge:.2f}")
    elif seat_type == 1:
        print(f"Seat surcharge (Regular): +Rs {surcharge:.2f}")        
    current_price += surcharge    
    if current_price > 500.0:
        gst_rate = 0.18
        gst_amount = current_price * gst_rate
        print(f"GST (18%): +Rs {gst_amount:.2f}")
    else:
        gst_rate = 0.12
        gst_amount = current_price * gst_rate
        print(f"GST (12%): +Rs {gst_amount:.2f}")       
    final_price = current_price + gst_amount
    print(f"---")
    print(f"Final price: Rs {final_price:.2f}")
    return final_price

if __name__ == "__main__":
    print("Welcome to Cinema Pricing Calculator")
    try:
        day = int(input("Enter Day of week (1-7, 1=Monday): "))
        time = int(input("Enter Show time (0-23): "))
        age = int(input("Enter Customer age: "))
        seat_type = int(input("Enter Seat type (1=Regular, 2=Premium, 3=Recliner): "))
        
        print("\n--- Itemized Breakdown ---")
        calculate_ticket_price(day, time, age, seat_type)
    except ValueError:
        print("Invalid input! Please enter integer values.")
