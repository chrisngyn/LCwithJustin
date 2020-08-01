"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

(...does Google really ask this?)
"""

def twoSum(nums, target):
    seen = {}

    for index in range(len(nums)):
        val = nums[index]

        if target - val in seen:
            return [index, seen[target - val]]
        else:
            seen[val] = index
    
    return []