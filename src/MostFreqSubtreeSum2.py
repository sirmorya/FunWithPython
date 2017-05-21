class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodeMap = {}
        self.findFrequentTreeSumHelper(root, nodeMap)
        maxVal = 0
        for key, value in nodeMap.items():
            maxVal = max(value, maxVal)
                
        result = []
        for key, value in nodeMap.items():
            if value == maxVal:
                result.append(key)
        return result
            
        
        
    def findFrequentTreeSumHelper(self, root, nodeMap):
        if root.left == None and root.right == None:
            val = nodeMap.get(root.val, 0)
            nodeMap[root.val] = val + 1
            return root.val
        lVal = self.findFrequentTreeSumHelper(root.left, nodeMap) if root.left != None else 0
        rVal = self.findFrequentTreeSumHelper(root.right, nodeMap) if root.right != None else 0
        sum = lVal + rVal + root.val
        val = nodeMap.get(sum, 0)
        nodeMap[sum] = val + 1
        return sum
 

class TreeNode(object):
    def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None
      
n2 = TreeNode(1)
n1 = TreeNode(1)
n1.left = n2
  
sol = Solution()
sol.findFrequentTreeSum(n1)