arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

freq = {}
intersection = []

for num in arr1:
    freq[num] = 1

for num in arr2:
    if num in freq and num not in intersection:
        intersection.append(num)

print(intersection)