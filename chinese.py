n=int(input())
day=list(map(int,input().split()))
night=list(map(int,input().split()))
k=int(input())

day.sort()
night.sort(reverse=True)
ans=0
for i in range(n):
    omins=day[i]+night[i]
    if omins>k:
        ans+=(omins-k)*100
        
print(ans)