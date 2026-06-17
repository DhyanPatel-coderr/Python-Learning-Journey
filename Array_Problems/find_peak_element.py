arr = [1, 100, 2]
first_element = arr[0]
found = False

for num in range(1,len(arr)-1):
    if arr[num - 1] < arr[num] and arr[num] > arr[num+1]:
        print(f"Peak element : {arr[num]}")
        found = True
        break

if not found:
    if arr[len(arr)-1] > first_element:
            largest = arr[len(arr)-1]
            print(largest)

    elif first_element == arr[0]:
            print(first_element)