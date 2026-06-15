num = 987654321

largest = -1
sec_largest = -1
third_largest = -1

while num != 0:
    rem = num % 10
    num = num // 10

    if rem > largest:
        third_largest = sec_largest
        sec_largest = largest
        largest = rem

    elif largest > rem > sec_largest:
        third_largest = sec_largest
        sec_largest = rem

    elif sec_largest > rem > third_largest:
        third_largest = rem

if third_largest == -1:
    print("No third largest exist.")
else:
    print(f"Third largest : {third_largest}")