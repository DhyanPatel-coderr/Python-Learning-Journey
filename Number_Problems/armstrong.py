def count_digits(num):
    if num == 0:
        return 1

    count = 0

    while num != 0:
        num = num // 10
        count += 1

    return count


def is_armstrong(num):
    temp = num
    armstrong = 0
    n = count_digits(num)

    while num != 0:
        rem = num % 10
        num = num // 10

        armstrong += rem ** n

    return temp == armstrong


print(is_armstrong(9474))