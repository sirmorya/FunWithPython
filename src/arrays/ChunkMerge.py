try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

class Triplet(object):
    def __init__(self, pos, val, index):
        self.pos = pos
        self.val = val
        self.index = index
        return
    def __cmp__(self, other):
        return self.val - other.val
    
class Solution(object):
    def chunkMerge(self, chunks):
        q = Q.PriorityQueue()
        for i in range(0, len(chunks)):
            q.put(Triplet(i, chunks[i][0], 1))
            
        res = []
        while(len(q) != 0):
            p = q.pop()
            res.append(p.val)
            if(p.index < len(chunks[p.pos])):
                p.val = chunks[p.pos][p.index]
                p.index = p.index + 1
                q.put(p)
        return res
        
sol = Solution()
print(sol.chunkMerge([[1,2,3],[4,5,6]]))
    
