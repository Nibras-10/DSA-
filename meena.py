n=int(input('enter the number of inputs'))

og=list(map(int,input().split()))
miss=list(map(int,input().split()))

print(sum(og)-sum(miss))
