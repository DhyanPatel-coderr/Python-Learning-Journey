arr = [1, 2, 2, 1]

left_sum = 0
right_sum = 0
total_sum = 0
found = False

for num in arr:
    total_sum += num

for num in range(len(arr)):
    right_sum = total_sum - arr[num] - left_sum

    if right_sum == left_sum:
        print(f"Equilibrium index and value : {num} and {arr[num]}")
        found = True
        break
    left_sum += arr[num]    

if not found:
    print("No equilibrium index")