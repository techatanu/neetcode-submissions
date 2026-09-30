class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit



'''
1)First remember that you to buy first and then sell
2) Create a min_price and set that to infinity
3) Check if prices[i] < min_price:
set prices[i] = min_price
4) set max_profit = 0
5) then check if prices[i] - min_price > max_profit:
set max_profit = prices[i] - min_price
6) Then return max_profit

'''

        