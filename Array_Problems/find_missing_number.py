arr = [1, 2, 3, 5, 6]
n = len(arr) + 1
exp_sum = 0
act_sum = 0

for num in range(arr[0],n+1):
    exp_sum += num

for num in arr:
    act_sum += num

print(exp_sum - act_sum)