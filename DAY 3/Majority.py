def majorityElement(arr):       
    candidate = None
    count = 0
    for i in arr:
        if count == 0:
            candidate = i
        if candidate == i: 
            count += 1 
        else: 
            count -= 1
    
    return candidate

print(majorityElement([2, 2, 1, 1, 1, 2, 2]))