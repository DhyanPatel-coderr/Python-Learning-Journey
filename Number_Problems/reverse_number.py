def reverse_number(num):
    rev = 0

    while num != 0:
        rem = num % 10
        num = num // 10

        rev = rev * 10 + rem

    return rev

print(f"Reverse : {reverse_number(12345)}")