v = 3
w = 10
half = (v+1)//2
i = 0

while i <= v:
    if ((half + i)*2 + (half - i)*4 == w and (half + i)+(half - i) <= v):
        print("2 wheel:", half+i, "4 wheel:", half-i)
        break
    elif ((half - i)*2 + (half + i)*4 == w and (half + i)+(half - i) <= v):
        print("2 wheel:", half-i, "4 wheel:", half+i)
        break
    else:
        i += 1
else:
    print("No solution")