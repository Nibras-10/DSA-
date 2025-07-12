def ans(ls, k, n):
    curr_sum = sum(ls[:k])
    max_sum = curr_sum
    for i in range(k, n):
        curr_sum = curr_sum - ls[i - k] + ls[i]
        max_sum = max(max_sum, curr_sum)
    return max_sum

s=ans([4, -1, 2, 5, 3], 3, 5)
print(s)