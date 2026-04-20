def calculate_minimum_notes(amount):
    
    denominations = [100, 50, 20, 10, 5, 2]
    
    
    note_counts = {}
    
    for note in denominations:
        if amount >= note:
            count = amount // note
            amount -= count * note
            note_counts[note] = count
            
    if amount > 0:
        print(f"Warning: Cannot give exact change. Remaining amount: {amount}rs")
        
    return note_counts

amount_to_return = 242

result = calculate_minimum_notes(amount_to_return)

print(f"To return {amount_to_return}rs, you need the following minimum notes:")
total_notes = 0
for note, count in result.items():
    print(f"- {count} note(s) of {note}rs")
    total_notes += count

print(f"\nTotal notes given: {total_notes}")

