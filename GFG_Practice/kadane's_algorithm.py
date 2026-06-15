# Problem : Find maximum subarray sum
# Platform : GeeksforGeeks

class Solution:
    def maxSubarraySum(self, arr):
        current_sum = 0
        max_sum = arr[0]

        for num in arr:
            current_sum += num

            if max_sum < current_sum:
                max_sum = current_sum

            if current_sum < 0:
                current_sum = 0

        return max_sum


arr = [2, 3, -8, 7, -1, 2, 3]

obj = Solution()

print("Maximum Subarray Sum :", obj.maxSubarraySum(arr))