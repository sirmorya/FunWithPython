class WordNode(object):
    def __init__(self, wrd, numSteps, pre):
        self.wrd = wrd
        self.numSteps = numSteps
        self.pre = pre
        
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        minStep = 0
        visited = []
        unvisited = []
        wordList.append(endWord)
        for wrd in wordList:
            unvisited.append(wrd)
        queue = []
        queue.append(WordNode(beginWord, 1, None))
        preNumSteps = 0
        result = []
        
        while len(queue) != 0:
            top = queue.pop(0)
            word = top.wrd
            currNumSteps = top.numSteps
            
            if word == endWord:
                if minStep == 0:
                    minStep = top.numSteps
                
                if top.numSteps <= minStep and minStep != 0:
                    t = []
                    t.append(word)
                    while top.pre != None:
                        t.append(0, top.wrd)
                        top = top.pre
                    result.append(t)
                    continue
        
            if preNumSteps < currNumSteps:
                for visitedWord in visited:
                    unvisited.remove(visitedWord)
                    
            preNumSteps = currNumSteps
            
            arr = list(word)
            
            for i in range(0, len(arr)):
                e = arr[i]
                for j in range(97, 110):
                    c = chr(j)
                    arr[i] = c
                    newWord = ''.join(arr)
                    if newWord in unvisited:
                        queue.append(WordNode(newWord, top.numSteps + 1, top))
                        visited.append(newWord)
                    arr[i] = e
                    
        return result  
     
sol = Solution()
print(sol.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
            
            
