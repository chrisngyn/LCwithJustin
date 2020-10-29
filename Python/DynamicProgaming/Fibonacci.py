# if N == 0:
#     return 0
# elif N == 1 or N == 2:
#     return 1
# else:
#     return self.fib(N - 1) + self.fib(N - 2)

class Solution:
    def fib(self, N: int) -> int:
        dp_solns = [-1 for _ in range(N + 1)]  # list comprehension - N + 1 so its inclusive of N
        return self.fib_helper(N, dp_solns)
    
    
    # MEMOIZATION - TOP TO DOWN - N TO 0
    def fib_helper(self, N, dp_solns):
        if N < 2:
            return N
        elif dp_solns[N] == -1:
                dp_solns[N] = self.fib_helper(N-1, dp_solns) + self.fib_helper(N-2, dp_solns)
        
        return dp_solns[N]

# --------------------------------

# TABULATION - SMALL PROBLEMS --> BIG PROBLEMS

class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        
        dp_solns = [0, 1]
        
        for i in range(2, N + 1):  # N + 1 to make it inclusive
            soln = dp_solns[i - 1] + dp_solns[i - 2]
            dp_solns.append(soln)
            
        return dp_solns[N]

# --------------------------------

# space optimization

class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        
        cache_1 = 0
        cache_2 = 1
        
        for i in range(2, N + 1):
            temp = cache_1 + cache_2
            cache_1 = cache_2
            cache_2 = temp
        
        return cache_2