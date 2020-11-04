"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Input: nums = [1,1,2]
Output: 2, nums = [1,2]

Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.
"""

"""
one set to arr[0] and one set to arr[1]

if arr[0] == arr[1], there's a duplicate, so just don't do anything (next it'll compare arr[0] to arr[2])

but if arr[1] != arr[1], we'll set arr[0] to arr[1] so we can check if arr[1] == arr[2]

return slow pointer + 1. if [0, 1, 2, 3] is sorted, slow pointer points to 3 but length is 4
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        
        for p2 in range(1, len(nums)):
            if nums[p1] == nums[p2]:  # a duplicate value, so don't increment
                pass
            else:  # not a duplicate, so we want to increment p1 (and also set p1 to current p2)
                p1 += 1
                nums[p1] = nums[p2]
        
        return p1 + 1
