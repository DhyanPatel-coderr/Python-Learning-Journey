arr = [10, -5, 20, -8, 0, 15, -2]
count_pos = 0
count_neg = 0
count_zero = 0

for num in arr:
    if num > 0:
        count_pos += 1
    elif num < 0:
        count_neg += 1
    else:
        count_zero += 1

print(f"Positive count : {count_pos}")
print(f"Negative count : {count_neg}")
print(f"Zeroes count : {count_zero}")