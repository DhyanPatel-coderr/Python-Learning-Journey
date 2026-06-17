arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

union = []

for num in arr1:
    if num not in union:
        union.append(num)

for num in arr2:
    if num not in union:
        union.append(num)

print(union)