n=int(input('enter the number of inputs'))
ls=[]
count=0
for i in range(n):
    s=list(map(int,input().split()))
    ls.append(s)

count=1
start=ls[0][1]
for i in range(1,n):
    if ls[i][0]>=start:
        count+=1
        start=ls[i][1]

print('number of shows completed: ',count)



    




