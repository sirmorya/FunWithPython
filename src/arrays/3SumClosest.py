class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_elem = sys.maxint
        res = 0
        for i in range(0, len(nums)):
            j = i + 1
            k = len(nums)-1
            while(j < k):
                s = nums[i] + nums[j] + nums[k]
                diff = abs(target -s)
                if(diff == 0):
                    return s
                if(diff<min_elem):
                    min_elem = diff
                    res = s
                if(s <= target):
                    j = j+1
                else:
                    k = k - 1
        return res
            
            