class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        
        """
        if len(prerequisites) == 0:
            return True
        
        counter = [0]*numCourses
        for i in range(0, len(prerequisites)):
            counter[prerequisites[i][0]] = counter[prerequisites[i][0]]+1
            
        queue = []
        numPre = 0
        for i in range(0, numCourses):
            if counter[i] == 0:
                queue.append(i)
                numPre = numPre + 1
                
        while len(queue) != 0:
            top = queue.pop(0)
            for i in range(0, len(prerequisites)):
                if prerequisites[i][1] == top:
                     counter[prerequisites[i][0]] = counter[prerequisites[i][0]] - 1
                     if counter[prerequisites[i][0]] == 0:
                         numPre = numPre + 1
                         queue.append(prerequisites[i][0])
                         
        return numPre == numCourses