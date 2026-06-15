def is_palindrome(num):
    temp = num
    rev = 0

    while num != 0:
        rem = num % 10
        num = num // 10

        rev = rev * 10 + rem

    return rev == temp

print(is_palindrome(12321))