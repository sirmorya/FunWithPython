class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.helper(result, [], a, 0)
        return result
        
    def helper(self, result, list, a, id):
        if(len(list) > 1):
            result.append(list)
        unique = []
        for i in range(id, len(a)):
            if (id > 0 and a[i] < a[id-1]):
                continue
            if a[i] in unique:
                continue
            unique.append(a[i])
            list.append(a[i])
            self.helper(result, list, a, i+1)
            list.pop()