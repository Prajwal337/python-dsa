def productexpect(arr):
    n=len(arr)
    if n==0:
        return []
    left=[1]*n
    right=[1]*n
    for i in range(1,n):
        left[i]=left[i-1]*arr[i-1]
    for i in range(n-2,-1,-1):
        right[i]=right[i+1]*arr[i+1]
    result=[0]*n
    for i in range(n):
        result[i]=left[i]*right[i]
    return result

arr=[1,2,3,4]
print(productexpect(arr))