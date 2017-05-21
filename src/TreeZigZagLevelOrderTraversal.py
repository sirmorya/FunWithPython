class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root == None:
            return result
        l1 = []
        l1.append(root)
        
        isReverse = True
        while len(l1) > 0:
            levelResult = []
            l2 = []
            while len(l1) > 0:
                node = l1.pop()
                levelResult.append(node.val)
                if isReverse:
                    if node.left != None:
                        l2.append(node.left)
                    if node.right != None:
                        l2.append(node.right)
                else:
                    if node.right != None:
                        l2.append(node.right)
                    if node.left != None:
                        l2.append(node.left)    
            l1 = l2
            result.append(levelResult)
            isReverse = not isReverse
        return result   
    
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

print(Solution().zigzagLevelOrder(n1))
