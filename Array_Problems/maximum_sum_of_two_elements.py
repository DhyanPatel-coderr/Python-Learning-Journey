arr = [5,5,5]

largest = float('-inf')
sec_largest = float('-inf')

if len(arr) == 1:
    print("Not enough elements")
else:
    for num in arr:
        if largest < num:
            sec_largest = largest
            largest = num
        elif largest >= num and num > sec_largest:
            sec_largest = num

    print(f"Maximum sum of two elements : {largest + sec_largest}")