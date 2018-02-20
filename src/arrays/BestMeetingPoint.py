'''
Created on Feb 15, 2018

@author: ankitsirmorya
'''
class Solution:
    def minTotalDistance(self, a):
        if(len(a) == 0 or len(a[0])==0):
            return 0
        vert = []
        horz = []
        for i in range(0, len(a)):
            for j in range(0, len(a[0])):
                if(a[i][j] == 1):
                    vert.append(i)
                    horz.append(j)
        
        vert.sort()
        horz.sort()
        size = int(len(vert)/2)
        x = vert[size]
        y = vert[size]
        dist = 0
        for i in range(0, len(a)):
            for j in range(0, len(a[0])):
                if(a[i][j] == 1):
                    dist = dist + abs(x-i) + abs(y-j)
                    
        
        return dist

sol = Solution()
print(sol.minTotalDistance([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0],[0, 0, 1, 0, 0]]))