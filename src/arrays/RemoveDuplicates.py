class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(nums ==None or len(nums) == 0):
            return 0
        j = 0
        met = False
        for i in range(1, len(nums)):
            if(nums[i] != nums[j]):
                j = j + 1
                nums[j] = nums[i]
                met = False
            elif(not met):
                j = j + 1
                nums[j] = nums[i]
                met = True
        return j+1