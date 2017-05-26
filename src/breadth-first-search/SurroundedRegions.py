class Solution(object):
    def solve(self, board):
   
        
        if board == None or len(board) == 0 or len(board[0]) == 0:
            return
        
        m = len(board)
        n = len(board[0])
        
        for i in range(0,m):
            board[i] = list(board[i])
        
        for i in range(0,m):
            
            if board[i][0] == 'O':
                self.bfs(board, i, 0)
            
        for j in range(1,n):
            
            if board[m-1][j] == 'O':
                self.bfs( board, m-1, j)
                
        for i in range(1, m-1):
            if board[i][n-1] == 'O':
                self.bfs( board, i , n-1)
        
        for j in range(1, n):
            if board[0][j] == 'O':
                self.bfs( board, 0, j)
                
        for i in range(0,m):
            for j in range(0,n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '1':
                    board[i][j] = 'O'
        
    def bfs(self, board, i, j):
        queue = [[i,j]]
        dirs = [[-1, 0], [1,0],[0,1],[0,-1]]
        board[i][j] = '1'
        m = len(board)
        n = len(board[0])
        while len(queue) != 0:
            cord = queue.pop()
            for d in dirs:
                k = cord[0] + d[0]
                l = cord[1] + d[1]
                if k < 0 or k >= m or l < 0 or l >= n:
                    continue;
                if board[k][l] == 'O':
                    board[k][l] = '1'
                    queue.append([k,l])
    

sol= Solution()
sol.solve([list('XXXX'),list('XOOX'),list('XXOX'),list('XOXX')])   