arr = [1, 2, 3, 4, -1]

positive = []
negative = []
final_list = []

for num in arr:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

common = min(len(positive), len(negative))

for i in range(common):
    final_list.append(positive[i])
    final_list.append(negative[i])

for i in range(common, len(positive)):
    final_list.append(positive[i])

for i in range(common, len(negative)):
    final_list.append(negative[i])

print(final_list)