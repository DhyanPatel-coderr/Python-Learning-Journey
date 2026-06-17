arr = [1, 2, 3, 4]
freq= {}
found = False

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for num in freq:
    if freq[num] > len(arr)//2:
        print(f"Majority element : {num}")
        found = True
        break
if not found:
    print("No majority element")