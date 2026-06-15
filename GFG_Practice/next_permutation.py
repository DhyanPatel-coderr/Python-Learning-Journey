# Problem: Next Permutation
# Platform: GeeksforGeeks

class Solution:
    def nextPermutation(self, arr):
        pivot = -1
        n = len(arr)

        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break

        if pivot == -1:
            arr.reverse()
            return arr

        smallest_idx = pivot + 1

        for i in range(pivot + 1, n):
            if arr[i] > arr[pivot] and arr[i] <= arr[smallest_idx]:
                smallest_idx = i

        arr[smallest_idx], arr[pivot] = arr[pivot], arr[smallest_idx]

        left = pivot + 1
        right = n - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1

        return arr


obj = Solution()

arr = [1, 2, 3]

print(obj.nextPermutation(arr))