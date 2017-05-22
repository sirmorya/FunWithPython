'''i=n, count[n] = sum(count[0..k]*count[k+1...n]) 0 <= k < n-1'''
class Solution(object):
    def numTrees(self, n):
        a = [0] * (n+1)
        a[0] = 1
        a[1] = 1
        for i in range(2,n+1):
            for j in range(0, i):
                a[i] = a[i] + (a[j] * a[i-j-1])
        return a[n]