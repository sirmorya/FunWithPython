'''
Created on Jan 23, 2018

@author: ankitsirmorya
'''
class Solution(object):
    def productExceptSelf(self, a):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]
        for i in range(1, len(a)):
            res.append(res[i-1] * a[i-1])
        right = 1
        for j in range(len(a)-1, -1, -1):
            res[j] = right * res[j]
            right = right * a[j]
        return res
    
sol = Solution()
sol.productExceptSelf([1,2,3,4])