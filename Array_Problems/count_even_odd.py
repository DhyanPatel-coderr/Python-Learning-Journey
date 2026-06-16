arr = [10, 21, 32, 43, 54, 65]
count_odd = 0
count_even = 0

for num in arr:
    if num%2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f"Number of odd values : {count_odd}")
print(f"Number of even values : {count_even}")