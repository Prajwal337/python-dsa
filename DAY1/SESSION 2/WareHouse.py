N = int(input("Enter No of deleveris"))
dele = []
sum = 0
print("Enter deleveris")
for i in range(N):
    dele.append(int(input()))
    sum += dele[i]

print("Total: ",sum)
print("avg: ",sum//N)