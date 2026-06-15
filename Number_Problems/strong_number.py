def factorial(num):
    if num == 0 or num == 1:
        return 1

    return num * factorial(num - 1)


def is_strong(num):
    temp = num
    strong = 0

    while num != 0:
        rem = num % 10
        num = num // 10

        strong += factorial(rem)

    return temp == strong


print(is_strong(145))