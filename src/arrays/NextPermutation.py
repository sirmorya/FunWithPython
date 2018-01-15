class Solution(object):
    def nextPermutation(self, a):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if (a == None or len(a)<2):
            return
        p = 0
        for i in range(len(a)-1, 0,-1):
            if(a[i]>a[i-1]):
                p=i-1
                break
        q = 0
        for i in range(len(a)-1, p,-1):
            if(a[i]>a[p]):
                q = i
                break
        if(p == 0 and q ==0):
            self.reverse(a, 0, len(a)-1)
            return
        t = a[p]
        a[p] = a[q]
        a[q] = t
        if(p<len(a)-1):
            self.reverse(a, p+1, len(a)-1)
    
    def reverse(self, a, p, q):
        while(p < q):
            t = a[p]
            a[p] = a[q]
            a[q] = t
            p = p+1
            q = q-1
            
sol = Solution()
a = [1,3,2]
sol.nextPermutation(a)

