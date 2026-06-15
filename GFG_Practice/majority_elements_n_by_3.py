# Problem: Majority Elements (More than n/3 times)
# Platform: GeeksforGeeks

class Solution:
    def findMajority(self, arr):
        n = len(arr)
        freq = {}
        majority = []

        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for i in freq:
            if freq[i] > n / 3:
                majority.append(i)

        majority.sort()
        return majority


obj = Solution()

arr = [2, 2, 3, 1, 3, 2, 1, 1]

print(obj.findMajority(arr))