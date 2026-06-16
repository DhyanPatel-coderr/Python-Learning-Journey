arr = [12, 45, 7, 89, 23]

smallest = arr[0]
sec_smallest = float('inf')

for num in arr:
    if smallest > num:
        sec_smallest = smallest
        smallest = num
    elif smallest > num and num > sec_smallest:
        sec_smallest = num

if sec_smallest == float('inf'):
    print("No second smallest exist")
else:
    print(f"Second smallest element : {sec_smallest}")