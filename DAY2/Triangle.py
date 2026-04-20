  
rows = 4

for i in range(1, rows + 1):
    print("*" * i + " " * (2 * (rows - i)) + "*" * i)
 
for i in range(rows, 0, -1):
    print("*" * i + " " * (2 * (rows - i)) + "*" * i)



#triangle
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))


rows = 5
for i in range(rows, 0,-1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
    