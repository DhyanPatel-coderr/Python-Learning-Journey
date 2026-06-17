arr = [2, 3, 10, 6, 4, 8, 1]

min_so_far = arr[0]
cur_diff = arr[1] - arr[0]
max_diff = 0

for i in range(1,len(arr)):
    cur_diff = arr[i] - min_so_far

    if cur_diff > max_diff:
        max_diff = cur_diff
    if arr[i] < min_so_far:
        min_so_far = arr[i]

print(max_diff)