# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 1 2 step

class Solution:
    def __init__(self):
        pass

    # def climbStairs(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    
    #     if n == 1:
    #         return 1
        
    #     if n == 2:
    #         return 2

    #     return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs(self, n: int) -> int: # n = 4, range is 0 1 2 3
        if n == 0:
            return 0

        if n == 1:
            return 1

        first = 1
        second = 2

        for i in range(3, n + 1):
            third = first + second
            first = second 
            second = third

        return second
            
t1 = Solution()
t2 = Solution()
t3 = Solution()
print(t1.climbStairs(10))
print(t2.climbStairs(3))
print(t3.climbStairs(4))