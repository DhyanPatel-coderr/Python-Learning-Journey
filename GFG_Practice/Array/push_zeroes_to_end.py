# Problem: Push Zeros to End
# Platform: GeeksforGeeks

class Solution:
    def pushZerosToEnd(self, arr):
        pos = 0

        for i in range(len(arr)):
            if arr[i] != 0:
                arr[pos], arr[i] = arr[i], arr[pos]
                pos += 1

        return arr


obj = Solution()

arr = [1, 0, 2, 0, 4, 0, 5]

print(obj.pushZerosToEnd(arr))