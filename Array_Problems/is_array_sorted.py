arr = [10, 20, 30, 40, 50]
is_sorted = True

for num in range(1,len(arr)):
    if arr[num - 1] > arr[num]:
        is_sorted = False
        break

if is_sorted:
    print("Array is sorted")
else:
    print("Array is not sorted")