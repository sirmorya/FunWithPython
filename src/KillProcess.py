class Node(object):
     def __init__(self, x):
         self.val = x
         self.children = []
            
class Solution(object):
                
    def killProcess(self, pid, ppid, kill):
        nodeMap = {}
        for id in pid:
            nodeMap[id] = Node(id)
        
        for idx in range(len(pid)):
            if ppid[idx] != 0:
                nodeMap[ppid[idx]].children.append(nodeMap[pid[idx]])
                
        res = []
        self.dfs(nodeMap[kill], res)
        return res
    
    def dfs(self, root, res):
        if root == None: return
        res.append(root.val)
        for n in root.children:
            self.dfs(n, res)
        
        
        