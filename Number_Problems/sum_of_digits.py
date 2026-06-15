def sum_of_digits(num):
    digit_sum = 0

    while num != 0:
        rem = num % 10
        num = num // 10

        digit_sum += rem

    return digit_sum

print(sum_of_digits(12345))