arr = [12, 45, 7, 89, 23]

if len(arr) == 0:
    print("Array is empty")
else:
    smallest = arr[0]

    for num in arr:
        if smallest > num:
            smallest = num

    print(f"Smallest element : {smallest}")