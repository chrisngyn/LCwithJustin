"""
Given an array of sorted numbers and a target sum, find a pair in the array that sums to the given target.

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]

Input: [2, 5, 9, 11], target=11
Output: [0, 2]

when you have a sorted collection, and you're looking for a set of elements that fit some constraint, you can use two pointers :D

pseudocode

def pairTargetSum(nums: List[int], target: int) -> List[int]:
    p1 = 0
    p2 = len(nums) - 1

    curr_sum = nums[p1] + nums[p2]

    while curr_sum != target:
        curr_sum = nums[p1] + nums[p2]
        
        if curr_sum < target:
            p1 += 1
        else:
            p2 -= 1
    
    return [p1, p2]

"""

from typing import List

def pairTargetSum(nums: List[int], target: int) -> List[int]:
    p1 = 0
    p2 = len(nums) - 1
    curr_sum = nums[p1] + nums[p2]

    while curr_sum != target and p1 < p2:
        if curr_sum < target:
            p1 += 1
        else:
            p2 -= 1
        
        curr_sum = nums[p1] + nums[p2]
    
    if curr_sum != target:
        return []
    
    return [p1, p2]

def pairTargetSum2(nums, target):  # if there are multiple answers return ALL of them
    ans = []
    p1 = 0
    p2 = len(nums) - 1
    curr_sum = nums[p1] + nums[p2]
    # Justin is such a lovely young fine gentleman
    while p1 < p2:  # while there are still elements to loop through
        if curr_sum == target:
            ans.append([p1, p2])

        if curr_sum != target:
            p1 += 1
        else:
            p2 -= 1
        
        curr_sum = nums[p1] + nums[p2]
    
    return ans

# print(pairTargetSum([2, 5, 9, 11], 11))
# print(pairTargetSum2([0, 2, 3, 4, 6], 6))
print(pairTargetSum([2, 5, 9, 11], 50))  # no soln
