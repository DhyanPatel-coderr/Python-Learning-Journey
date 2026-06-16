arr = [16, 17, 4, 3, 5, 2]
n = len(arr) -1
leader = float('-inf')
leader_arr = []

for num in range(n, -1, -1):
    if leader < arr[num]:
        leader = arr[num]
        leader_arr.append(leader)

for num in range(len(leader_arr)-1,-1,-1):
    print(leader_arr[num])