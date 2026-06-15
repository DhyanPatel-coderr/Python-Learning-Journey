num = 1112233333444455
max_run = -1
max_digit = 0
cur_run = 0
cur_dig = 0

while num != 0:
    rem = num%10
    num = num//10

    if rem == cur_dig :
        cur_run += 1
    else:
        if max_run < cur_run:
            max_run = cur_run
            max_digit = cur_dig
            
        cur_dig = rem
        cur_run = 1

if max_run < cur_run:
    max_run = cur_run
    max_digit = cur_dig

print(f"Digit with longest consecutive run : {max_digit}")
print(f"Run length : {max_run}")