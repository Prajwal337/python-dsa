def moreelemments(arr):
    k=len(arr)//2
    for i in arr:
        if arr.count(i) > k:
            return i
    return None
arr=[3,3,4,2,4,4,2,4,4]
print(moreelemments(arr))



















