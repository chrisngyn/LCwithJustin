"""
you can make as many transactions as you want this time

so again, keep track of a 'current_min' up to where we are at in the array

if the next value is > current_min, make a transaction and set current_min to the value we just subtracted from

if the next value is < current_min, set current_min to the value
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        current_min = float('inf')
        
        for index in range(len(prices)):
            val = prices[index]
            
            if val >= current_min:
                ret += val - current_min
                current_min = val
            else:
                current_min = val
                
        return ret
