arr = [10, 0, 20, 0, 30, 40]
pos = 0

for num in range(0,len(arr)):
    if arr[num] != 0:
        arr[pos], arr[num] = arr[num], arr[pos]
        pos += 1

print(arr)