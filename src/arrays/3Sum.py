class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(0,len(nums)):
            self.twosum(nums, res, i+1, -nums[i], nums[i])
        return res
        
    def twosum(self, nums, res, start, target, e):
        j = len(nums)-1
        i = start
        while (i < j):
            s = nums[i] + nums[j]
            if(s == target):
                elem = [e, nums[i],nums[j]]
                if elem not in res:
                    res.append(elem)
                i = i +1;
                j = j - 1;
            elif(s < target):
                i = i + 1
            else:
                j = j -1
                
sol = Solution()
sol.threeSum([-1,0,1,2,-1,-4])