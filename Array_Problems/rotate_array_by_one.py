arr = [10, 20, 30, 40, 50]
n = len(arr) -1

for num in range(n, 0, -1):
    arr[num-1], arr[num] = arr[num], arr[num-1]

print(arr)    