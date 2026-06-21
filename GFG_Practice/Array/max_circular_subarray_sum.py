# Problem : Find maximum circular subarray sum
# Platform : GeeksforGeeks

class Solution:
    def maxCircularSum(self, arr):
        current_max = arr[0]
        max_sum = arr[0]
        current_min = arr[0]
        total_sum = arr[0]
        min_sum = arr[0]

        for num in arr[1:]:
            total_sum += num

            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)

            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)

        if max_sum < 0:
            return max_sum

        circular_sum = total_sum - min_sum
        return max(max_sum, circular_sum)


arr = [8, -8, 9, -9, 10, -11, 12]

obj = Solution()
print("Maximum Circular Subarray Sum:", obj.maxCircularSum(arr))