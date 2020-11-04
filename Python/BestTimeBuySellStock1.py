"""
keep a track of the current smallest min up to a point

try to subtract it from every value in front of it if it's larger

if it's smaller than current min, we have a new current min
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        current_min = float('inf')
        
        for index in range(len(prices)):
            val = prices[index]
            
            if val >= current_min:
                ret = max(ret, val - current_min)
            else:
                current_min = val
        
        return ret
