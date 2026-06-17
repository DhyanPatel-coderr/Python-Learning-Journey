arr = [2, 0, 4, 5]
result = []

for i in range(len(arr)):
    prod = 1

    for j in range(len(arr)):
        if i != j:
            prod *= arr[j]

    result.append(prod)
print(result)