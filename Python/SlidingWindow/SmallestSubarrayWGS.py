"""
Given an array of positive numbers and a positive number ‘K’, 
find the length of the smallest contiguous subarray whose sum is 
greater than or equal to ‘K’. Return 0, if no such subarray exists.

Input: [2, 1, 5, 2, 3, 2], K=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
"""

import sys
import math

def smallest_subarray_with_given_sum(k, arr):
    ret = sys.maxsize
    sum, start_index = 0, 0

    for end_index in range(len(arr)):  # [2, 1, 5, 2, 3, 2] --> [0, 1, 2, 3, 4, 5]
        sum += arr[end_index]
        
        while sum >= k:  # WHILE the sum is greater than K, keep popping shit off. don't pop off once, cuz sum could still be greater!
            ret = min(end_index - start_index + 1, ret)            
            sum -= arr[start_index]
            start_index += 1
    
    return ret

    # ret = sys.maxsize
    # sum = 0
    # start_index = 0
    # num_element = 0

    # for end_index in range(len(arr)):  # [2, 1, 5, 2, 3, 2] --> [0, 1, 2, 3, 4, 5]
    #     if sum < k:
    #         sum += arr[end_index]
    #         num_element += 1
        
    #     while sum >= k:  # WHILE the sum is greater than K, keep popping shit off. don't pop off once, cuz sum could still be greater!
    #         if num_element < ret:
    #             ret = num_element
            
    #         sum -= arr[start_index]
    #         start_index += 1
    #         num_element -= 1
    
    # return ret

print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))  # 2
print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))  # 1
print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))  # 3
