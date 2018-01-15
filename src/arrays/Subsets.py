import math
class Solution(object):
    def subsets(self, nums):
        res = []
        if(nums == None or len(nums) == 0):
            return res
        n = int(math.pow(2, len(nums)))-1
        while ( n >= 0):
            num = n
            l = []
            for i in range(0, len(nums)):
                if((num & 1) == 1):
                    l.append(nums[i])
                num = num >> 1
                    
            res.append(l)
            n = n - 1
        return res
        
sol = Solution()
nums = [1,2,3]
res = sol.subsets(nums)
print(res)