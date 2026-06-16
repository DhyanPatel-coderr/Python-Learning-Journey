arr = [10, 20, 10, 30, 20, 10]
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for i in freq:
    print(f"{i} : {freq[i]}")