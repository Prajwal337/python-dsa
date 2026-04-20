pils = [5,8,10]
h = 6
k= len(pils)
print(len(pils))
def cal(pil, h, k):
    pil
    j = 0
    for i in range(h):
        pil[j] = pil[j] - k
        if(pil[j] <=0 and j < len(pils)-1):
            j +=1
    print(pil)
    if(pil[j]>0):
        return -1
    else:
        return k

while(1):
    k=cal(pils,h,k+1)
    if(k>0):
        print("k:-",k);break