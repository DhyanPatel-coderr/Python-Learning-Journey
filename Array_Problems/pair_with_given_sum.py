arr = [1,2,5,8,9]
target = 13

seen = {}
found = False

for num in arr:
    needed = target - num
    if needed in seen:
        print(f"Pair found : {needed},{num}")
        found = True
        break
    else:
        seen[num] = 1

if not found:
    print("No pair")