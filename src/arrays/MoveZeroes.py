class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(0, len(nums)):
            if (nums[i] != 0) :
                nums[j] = nums[i]
                j = j + 1
        for i in range(j, len(nums)):
            nums[j] = 0

s = Solution()
s.moveZeroes([0,3,4,5,9,0,0])