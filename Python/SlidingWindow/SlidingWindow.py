"""
when you have an array / linked list and asked to calculate / find something among all the possible contiguous subarrays / sublists
of a given size

think about algorithms / patterns in terms of: do they meet the conditions for me to apply them

Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], find average of all subarrays of size 5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]

for i in range(len(arr)) --> 0 1 2 3 4 5 6 7 8
"""

from typing import List

# BRUTE FORCE - O(n * k)
# def sliding_window(arr: List[int], k: int) -> List[int]:
#     ret = []
#     # k = 5
#     for i in range((len(arr) - k) + 1):  # range(len(arr)) --> [0, 1, 2, 3, 4, 5, 6, 7, 8] <-- this is just a stopping point
#         sum = 0.0                        # range(len(arr) - k + 1) --> [0, 1, 2, 3, 4] --> [4, 5, 6, 7, 8] <-- stop when theres less than 5
#         for j in range(i, i + k):  # [0, 1, 2, 3, 4]
#             sum += arr[j]
#         ret.append(sum / k)

#     return ret

# SLIDING WINDOW - O(n)
def sliding_window(arr: List[int], k: int) -> List[int]:
    ret = []
    window_sum, window_start = 0.0, 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # increase your window by one (add next element)
        if window_end >= k - 1:  # first get k elements
            ret.append(window_sum / k)  # add
            window_sum -= arr[window_start]  # shrink your window by one (cut oldest element)
            window_start += 1  # window_size --> 5, 4, 5, 4, 5, 4, 5

    return ret

print(sliding_window([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))