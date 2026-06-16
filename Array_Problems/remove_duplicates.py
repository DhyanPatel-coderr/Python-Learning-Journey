arr = [10, 20, 10, 30, 20, 40]
arr2 = []

for num in arr:
    if num not in arr2:
        arr2.append(num)

print(arr2)