arr=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def spiral(arr):
    result=[]
    while arr:
        result+=arr.pop(0)
        if arr and arr[0]:
            for i in arr:
                result.append(i.pop())
        if arr:
            result+=arr.pop()[::-1]
        if arr and arr[0]:
            for i in arr[::-1]:
                result.append(i.pop(0))
    return result

print(spiral(arr))