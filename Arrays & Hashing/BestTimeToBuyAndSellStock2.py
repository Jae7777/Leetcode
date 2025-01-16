# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        held = prices[0]
        profits = 0
        for price in prices[1:]:
            if price <= held:
                held = price
            else:
                profits += price - held
                held = price
        return profits