n,s=list(map(int,input().split()))
ls=list(map(int,input().split()))

ls.sort(reverse=True)
print(sum(ls[:s]))