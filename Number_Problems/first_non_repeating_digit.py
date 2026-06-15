num = 1234215
freq = {}
non_repeating_digit  = 0

while num != 0:
    rem = num%10
    num = num//10

    if rem in freq:
        freq[rem] += 1
    else:
        freq[rem] = 1

for i in freq:
    if freq[i] == 1 :
        non_repeating_digit = i

if non_repeating_digit == 0:
    print("No non-repeating digit found.")
else:
    print(f"First Non repeating digit : {non_repeating_digit}")