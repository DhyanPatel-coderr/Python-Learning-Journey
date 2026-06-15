def largest_digit(num):
    largest = -1

    while num != 0:
        rem = num % 10
        num = num // 10

        if largest < rem:
            largest = rem

    return largest

print(f"Largest digit : {largest_digit(583721)}")