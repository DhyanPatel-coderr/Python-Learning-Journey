# Problem: Second Largest Element
# Platform: GeeksforGeeks

class Solution:
    def getSecondLargest(self, arr):
        largest = arr[0]
        second_largest = -1
        
        for i in arr:
            if largest < i:
                second_largest = largest
                largest = i
        
            elif second_largest < i and i < largest:
                second_largest = i
        return second_largest
    
obj = Solution()

arr = [12, 35, 1, 10, 34, 1]

print(obj.getSecondLargest(arr))