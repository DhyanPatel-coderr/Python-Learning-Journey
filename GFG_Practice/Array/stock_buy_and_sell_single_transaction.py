# Problem: Stock Buy and Sell – Maximum Profit (Single Transaction)
# Platform: GeeksforGeeks

class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        smallest = prices[0]

        for i in prices:
            if smallest > i:
                smallest = i

            profit = i - smallest

            if profit > max_profit:
                max_profit = profit

        return max_profit


obj = Solution()

prices = [7, 1, 5, 3, 6, 4]

print(obj.maxProfit(prices))