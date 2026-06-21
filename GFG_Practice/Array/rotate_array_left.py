# Problem: Rotate Array by D Elements (Left Rotation)
# Platform: GeeksforGeeks

class Solution:
    def rotateArr(self, arr, d):
        d = d % len(arr)

        temp = arr[:d]

        for i in range(d, len(arr)):
            arr[i - d] = arr[i]

        for i in range(d):
            arr[len(arr) - d + i] = temp[i]

        return arr


obj = Solution()

arr = [1, 2, 3, 4, 5]
d = 2

print(obj.rotateArr(arr, d))