arr = [1, 1, 2, 2, 2, 3, 3, 4]

cur_digit = 0
cur_run = 0
max_digit = -1
max_run = 0

for num in arr:
    if num == cur_digit:
        cur_run += 1
    else:
        if max_run < cur_run:
            max_run = cur_run
            max_digit = cur_digit
        cur_digit = num
        cur_run = 1

if max_run < cur_run:
    max_run = cur_run
    max_digit = cur_digit

print(f"Digit with longest consecutive run : {max_digit}")
print(f"Longest run : {max_run}")