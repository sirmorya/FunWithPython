'''
Created on Jan 15, 2018

@author: ankitsirmorya
'''
class Solution(object):
    def sortColors(self, nums):
        j = self.sortColor(nums, 0, len(nums), 0)
        self.sortColor(nums, j, len(nums), 1)
        
    def sortColor(self, nums, start, end, elem):
        j = start
        for i in range(start,end):
            if(nums[i] == elem):
                t = nums[j]
                nums[j] = elem
                nums[i] = t
                j = j + 1
        return j
    
sol = Solution()
sol.sortColors([0,1,2,0,1,2,0,2,1])