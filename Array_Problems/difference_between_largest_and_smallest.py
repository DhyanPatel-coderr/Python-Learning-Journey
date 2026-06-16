arr = [12, 45, 7, 89, 23]
largest = arr[0]
smallest = arr[0]

for num in arr:
    if largest < num:
        largest = num
    if smallest > num:
        smallest = num

print(f"Largest : {largest}")
print(f"Smallest : {smallest}")
print(f"Difference : {largest - smallest}")