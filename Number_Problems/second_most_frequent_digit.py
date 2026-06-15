num = 11122233
most_freq = -1
sec_most_freq = -1
count = -1
sec_count = -1
freq = {}

while num != 0:
    rem = num%10
    num = num//10

    if rem in freq:
        freq[rem] += 1
    else:
        freq[rem] = 1

for i in freq:
    if count < freq[i]:
        sec_most_freq = most_freq
        most_freq = i
        sec_count = count
        count = freq[i]
    elif count > freq[i] and freq[i] > sec_count:
        sec_most_freq = i
        sec_count = freq[i]

if count == sec_count or sec_count == -1:
    print("No second most frequent digit.")
else:
    print(f"Second most frequent digit : {sec_most_freq}")
    print(f"Count : {sec_count}")