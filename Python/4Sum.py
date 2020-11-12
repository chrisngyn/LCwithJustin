class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        nums.sort()
        print(nums)
        
        for p1 in range(len(nums) - 3):
            if p1 > 0 and nums[p1] == nums[p1 - 1]:
                continue
            
            for p2 in range(p1 + 1, len(nums) - 2):
                if p2 > 1 and nums[p2] == nums[p2 - 1] and p2 != p1 + 1:  # hacky slashy 3rd condition, but works!
                    continue
                    
                p3 = p2 + 1
                p4 = len(nums) - 1
                
                while p3 < p4:
                    val = nums[p1] + nums[p2] + nums[p3] + nums[p4]
                    
                    if val == target:
                        ret.append([nums[p1], nums[p2], nums[p3], nums[p4]])
                        
                        p3 += 1
                        while p3 < p4 and nums[p3] == nums[p3 - 1]:
                            p3 += 1
                        
                        p4 -= 1
                        while p3 < p4 and nums[p4] == nums[p4 + 1]:
                            p4 -= 1
                        
                    elif val < target:
                        p3 += 1
                    else:
                        p4 -= 1
        
        return ret
