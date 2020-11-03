"""
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Input: height = [4,3,2,1,4]
Output: 16

we can solve this with two pointers. have one on each end, take the min of either pointer, and set the volume to
(that min * (distance between p2 and p1)). increment / decrement whichever of the two pointers is the smallest
keep a running maximum value
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ret = 0
        p1 = 0
        p2 = len(height) - 1
        
        while p1 < p2:
            value = min(height[p1], height[p2])
            container = value * (p2 - p1)
            ret = max(ret, container)
            
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        
        return ret
