# Problem : Find maximum product subarray
# Platform : GeeksforGeeks

class Solution:
    def maxProduct(self, arr):
        current_max = arr[0]
        current_min = arr[0]
        max_prod = arr[0]

        for num in arr[1:]:
            new_max = max(num, current_max * num, current_min * num)
            new_min = min(num, current_max * num, current_min * num)

            current_max = new_max
            current_min = new_min

            if max_prod < current_max:
                max_prod = current_max

        return max_prod


arr = [-2, 6, -3, -10, 0, 2]

obj = Solution()

print("Maximum Product Subarray :", obj.maxProduct(arr))