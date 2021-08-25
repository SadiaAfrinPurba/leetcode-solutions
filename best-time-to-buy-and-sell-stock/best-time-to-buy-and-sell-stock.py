class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        minimum = prices[0]
        
        for price in prices[1:]:
            if price < minimum:
                minimum = price
                
            else:
                maximum = max(maximum, price - minimum)
                
        return maximum
        