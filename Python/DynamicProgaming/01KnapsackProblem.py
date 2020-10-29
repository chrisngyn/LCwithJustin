"""
Given weights and values of n items, put these items in a knapsack of capacity
W to get the maximum total value in the knapsack. In other words, given two
integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights
associated with n items respectively. Also given an integer W which represents
knapsack capacity, find out the maximum value subset of val[] such that sum of
the weights of this subset is smaller than or equal to W. You cannot break an 
item, either pick the complete item or don’t pick it (0-1 property).
"""

def solve_knapsack(profits, weights, capacity):
    return solve_knapsack_recursive(profits, weights, capacity, 0)


def solve_knapsack_recursive(profits, weights, capacity, current_index):
    if current_index >= len(weights) or capacity == 0:
        return 0

    s1, s2 = 0, 0  # s1 = pick, s2 = don't pick

    if weights[current_index] <= capacity:
        s1 = profits[current_index] + solve_knapsack_recursive(profits, weights, capacity - weights[current_index], current_index + 1)  # choose
    
    s2 = solve_knapsack_recursive(profits, weights, capacity, current_index + 1)  # no choose

    return max(s1, s2)


print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))  # 22: 6 + 16
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))  # 17: 1 + 6 + 10
