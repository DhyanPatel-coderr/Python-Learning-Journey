arr = [5, 2, 9, 1]
largest = arr[0]
second_largest = float("-inf")

for i in arr:
    if largest < i:
        second_largest = largest
        largest = i
    elif largest > i and i > second_largest:
        second_largest = i

if second_largest == float("-inf"):
    print("No second largest element exist")
else:
    print(f"Second largest element : {second_largest}")