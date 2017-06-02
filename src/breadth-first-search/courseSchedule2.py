class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        if len(prerequisites) == 0:
            res = [0]*numCourses
            for m in range(0, numCourses):
                res[m] = m
            return res
        
        pCounter = [0]*numCourses
        for i in range(0, len(prerequisites)):
            pCounter[prerequisites[i][0]] = pCounter[prerequisites[i][0]] + 1
            
        queue = []
        numNoPre = 0
        
        for i in range(0, numCourses):
            if pCounter[i] == 0:
                queue.append(i)
                numNoPre = numNoPre + 1
                
        res = []
        
        while len(queue) != 0:
            c= queue.pop(0)
            res.append(c)
            
            for i in range(0, len(prerequisites)):
                if prerequisites[i][1] == c:
                    pCounter[prerequisites[i][0]] = pCounter[prerequisites[i][0]]-1
                    if pCounter[prerequisites[i][0]] == 0:
                        queue.append(prerequisites[i][0])
                        numNoPre = numNoPre + 1
                        
        if numNoPre == numCourses:
            return res
        else:
            return []
            
        
        