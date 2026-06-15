arr = [5, 2, 9, 1]
largest = arr[0]

for i in arr:
    if largest < i:
        largest = i
print(f"largest element : {largest}")