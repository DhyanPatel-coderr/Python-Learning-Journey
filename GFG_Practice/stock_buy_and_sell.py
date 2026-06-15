# Problem: Stock Buy and Sell – Multiple Transactions Allowed
# Platform: GeeksforGeeks

class Solution:
    def maxProfit(self, prices):
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])

        return profit


obj = Solution()

prices = [100, 180, 260, 310, 40, 535, 695]

print(obj.maxProfit(prices))