def kadane(ls):
    curr_sum=ls[0]
    max_sum=-99999
    for i in range(1,len(ls)):
        curr_sum=max(ls[i],curr_sum+ls[i])
        max_sum=max(max_sum,curr_sum)
    return max_sum

s=kadane([4, -1, 2, 5, 3])
print(s)
