name=input("enter the name")
mid=len(name)//2
firsthalf=name[:mid]
secondhalf=name[mid:]

frev=''.join(reversed(firsthalf))
srev=''.join(reversed(secondhalf))

result= frev+srev
print(result)