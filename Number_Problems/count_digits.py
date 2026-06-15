def count_digits(num):
    if num == 0:
        return 1

    count = 0

    while num != 0:
        num = num // 10
        count += 1

    return count

print(count_digits(583721))