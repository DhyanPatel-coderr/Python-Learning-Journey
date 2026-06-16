arr = [10, 20, 10, 30, 20, 40]
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
        
for num in arr:
    if freq[num] == 1:
        print(f"First non repeating element : {num}")
        break