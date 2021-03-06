"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

The solution set must not contain duplicate triplets.

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

pseudocode;

sort array first, [-1 0 1 2 -1 -4] becomes [-4 -1 -1 0 1 2]

ans = []

p1 = 0
p2 = len(nums) - 1
p3 = p1 + 1

while p1 < p2:
    while p3 < p2:
        sum = p1 + p2 + p3

        if sum == 0:
            ans.append()
            p3 += 1  # check first if p3 + 1 == p3, if so, then do p3 + 2, etc.
        elif sum > 0:
            p2 -= 1
        else:
            p3 += 1
    
    p1 += 1
    p2 = len(nums) - 1
    p3 = p1 + 1

while p3 < p2:
    sum = nums[p1] + nums[p2] + nums[p3]

    if sum == 0:
        ans.append([p1, p2, p3])

    if sum < 0:
        p3 += 1
    else:
        p2 -= 1

while nums[p1] == nums[p1+1] and p1 + 1 < len(nums):
    p1 += 1
"""

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:  # time O(n^2) and space O(1)
    ret = []

    if len(nums) < 3:
        return []

    nums.sort()  # O(n log n)

    for p1 in range(len(nums)):  # O(n)
        if (p1 > 0) and (nums[p1] == nums[p1 - 1]):  # skip this iteration, because p1 will be a duplicate value
            continue

        # if nums[p1] > 0:  # because you would never reach zero
        #     break
        
        p2 = p1 + 1
        p3 = len(nums) - 1
        val1 = nums[p1]

        while p2 < p3:  # O(n - 1) ~ O(n)
            val2 = nums[p2]
            val3 = nums[p3]
            total = val1 + val2 + val3

            if total == 0:
                ret.append([val1, val2, val3])

                while p2 < p3 and nums[p2] == nums[p2 + 1]:
                    p2 += 1
                p2 += 1

                while p3 > p2 and nums[p3] == nums[p3 - 1]:
                    p3 -= 1
                p3 -= 1
                
            elif total > 0:
                p3 -= 1
            else:
                p2 += 1

    return ret

print(threeSum([-2, -2, -1, 0, 1, 2]))
