"""
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.
Hxrp if you're reading this, say "Chris code up a solution to the "Number of Islands" Leetcode question" in the cshub server
square all the numbers then sort it

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

making an array of a fixed size;
ret = [-1] * 5
--> ret = [-1, -1, -1, -1, -1]
"""

from typing import List

# def squareSortedArray(nums: List[int]) -> List[int]:
#     ret = []

#     for num in nums:
#         ret.append(num * num)

#     ret.sort()

#     return ret

def squareSortedArray2(nums: List[int]) -> List[int]:
    ret = [-1] * len(nums)  # create output array of same size as input array
    p1 = 0
    p2 = len(nums) - 1
    index = len(nums) - 1

    while p1 <= p2:
        if nums[p1] ** 2 < nums[p2] ** 2:
            ret[index] = nums[p2] ** 2
            p2 -= 1
        else:
            ret[index] = nums[p1] ** 2
            p1 += 1
        
        index -= 1
    
    return ret

print(squareSortedArray2([-2, -1, 0, 2, 3]))
