# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

from typing import List

class Solution:
    def __init__(self):
        pass

    def twoSum(self, num: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(num)):
            if (target - num[i]) in dic:
                return [dic[target - num[i]], i]
            else:
                dic[num[i]] = i

        return -1

t1 = Solution()
t2 = Solution()
print(t1.twoSum([2, 7, 11, 15], 9))
print(t2.twoSum([1, 2, 3, 4, 5], 100))