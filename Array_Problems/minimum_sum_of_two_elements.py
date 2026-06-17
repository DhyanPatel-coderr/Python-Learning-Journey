arr = [10, 10, 10]

smallest = float('inf')
sec_smallest = float('inf')

if len(arr) == 1:
    print("Not enough element")
else:
    for num in arr:
        if smallest > num:
            sec_smallest = smallest
            smallest = num
        elif num >= smallest and sec_smallest > num:
            sec_smallest = num

    print(f"Minimum sum of two element : {smallest + sec_smallest}")