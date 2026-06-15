num = 1234321
freq = {}
most_freq = -1
count = -1

while num != 0:
    rem = num%10
    num = num//10

    if rem in freq:
        freq[rem] += 1
    else:
        freq[rem] = 1

for i in freq:
    if count < freq[i]:
        most_freq = i
        count = freq[i]
    elif count == freq[i] and i > most_freq:
        most_freq = i

print(f"Most frequent digit : {most_freq}")
print(f"Count : {count}")