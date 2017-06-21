class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        dirs = [[-1, 0], [1,0],[0,1],[0,-1],[-1,-1],[1,1],[-1,1],[1,-1]]
        
        m = len(board)
        n = len(board[0])
        
        queue = []
        queue.append(click)
        
        while len(queue) != 0:
            cell = queue.pop(0)
            
            if board[cell[0]][cell[1]] == 'M':
                board[cell[0]][cell[1]] = 'X'
                continue
            
            count = 0
            for d in dirs:
                r = cell[0] + d[0]
                c = cell[1] + d[1]
                if r<0 or r >= m or c < 0 or c >= n:
                    continue
                if board[r][c] == 'M' or board[r][c] == 'X':
                    count = count + 1
                    
            if count > 0:
                board[cell[0]][cell[1]] = str(count)
            
            else:
                board[cell[0]][cell[1]] = 'B'
                for d in dirs:
                    r = cell[0] + d[0]
                    c = cell[1] + d[1]
                    if r<0 or r >= m or c < 0 or c >= n:
                        continue
                    if board[r][c] == 'E':
                        queue.append([r,c])
                        board[r][c] = 'B'
        return board
                    