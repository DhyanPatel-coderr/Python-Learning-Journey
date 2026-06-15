num = 111222333

max_freq = -1
max_freq_dig = 0

min_freq = float("inf")
min_freq_dig = 0

freq = {}

while num != 0:
    rem = num % 10
    num = num // 10

    if rem in freq:
        freq[rem] += 1
    else:
        freq[rem] = 1

for i in freq:
    if max_freq < freq[i]:
        max_freq = freq[i]
        max_freq_dig = i

    elif max_freq == freq[i] and i > max_freq_dig:
        max_freq_dig = i

    if min_freq > freq[i]:
        min_freq = freq[i]
        min_freq_dig = i

    elif min_freq == freq[i] and i < min_freq_dig:
        min_freq_dig = i

print(f"Most frequent digit : {max_freq_dig}")
print(f"Least frequent digit : {min_freq_dig}")
print(f"Difference : {max_freq - min_freq}")