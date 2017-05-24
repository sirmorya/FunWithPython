'''https://leetcode.com/problems/01-matrix/'''
class Solution(object):
    def updateMatrix(self, matrix):
        m = matrix.length
        n = matrix[0].length
        
        queue = []
        for i in range(0,m):
            for j in  range(0,n):
                if matrix[i][j] == 0:
                    queue.append([i,j])
                else:
                    matrix[i][j] = sys.maxint
                    
        
        dirs = [[-1, 0], [1,0],[0,1],[0,-1]]
        
        while len(queue) > 0:
            cell = queue.poll(0)
            for d in dirs:
                r = cell[0] + d[0]
                c = cell[1] + d[1]
                if r<0 or r >=m or c < 0 or c >= n or matrix[r][c] <= matrix[cell[0]][cell[1]] + 1: continue
                '''if the newly calculated distance is  >= current distance then we don't need to explore the cell again'''
                queue.append([r,c])
                matrix[r][c] = matrix[cell[0]][cell[1]] + 1
        
        return matrix
        