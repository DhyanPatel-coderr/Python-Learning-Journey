# Problem: Minimize the Heights II
# Platform: GeeksforGeeks

class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)

        arr.sort()

        ans = arr[n - 1] - arr[0]

        for i in range(n - 1):
            if arr[i + 1] - k < 0:
                continue

            maximum = max(arr[i] + k, arr[n - 1] - k)
            minimum = min(arr[0] + k, arr[i + 1] - k)

            ans = min(ans, maximum - minimum)

        return ans


obj = Solution()

arr = [1, 5, 8, 10]
k = 2

print(obj.getMinDiff(arr, k))