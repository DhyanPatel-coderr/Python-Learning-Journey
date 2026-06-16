arr = [1, 1, 3, 2, 5]
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for num in arr:
    if freq[num] > 1:
        print(f"Duplicate element is {num}")
        break