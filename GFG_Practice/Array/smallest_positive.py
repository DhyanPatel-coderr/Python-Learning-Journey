# Problem : Find smallest positive number from array
# Platform : GeeksforGeeks

class Solution:
    def missingNumber(self, arr):
        missing = 1

        while missing in arr:
            missing += 1

        return missing


arr = [2, -3, 4, 1, 1, 7]

obj = Solution()
print(obj.missingNumber(arr))