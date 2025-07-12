def maxvalinwind(ls,k,n):
    ls2=[]
    s=-9999
    for i in range(0,n-k+1):
        wind=ls[i:k+i]
        s=max(s,max(wind))
        ls2.append(s)
        
    return ls2

s=maxvalinwind([4,7,9,2,-13,5,4,6,12,1], 3, 10)
print(s)

