class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res


# 240813: chose not sell on the same day if it's the lowest day
def maxProfit_me(self, prices: List[int]) -> int:
        lowest = prices[0]
        res = 0

        for price in prices:
            lowest = min(price, lowest)
            if price < lowest:
                lowest = price
            else:
                res = max(res, price - lowest)
        
        return res