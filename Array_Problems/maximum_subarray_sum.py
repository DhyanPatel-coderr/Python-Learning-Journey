arr = [-5, -2, -8]

cur_sum = 0
max_sum = arr[0]

for num in arr:
    cur_sum += num

    if max_sum < cur_sum:
        max_sum = cur_sum
    if cur_sum < 0:
        cur_sum = 0
    
print(max_sum)