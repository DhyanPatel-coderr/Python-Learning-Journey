num = 5487921

largest = -1
sec_largest = -1

while num != 0:
    rem = num % 10
    num = num // 10

    if largest < rem:
        sec_largest = largest
        largest = rem

    elif largest > rem and rem > sec_largest:
        sec_largest = rem

if sec_largest == -1:
    print("No second largest exist.")
else:
    print(f"Second largest : {sec_largest}")