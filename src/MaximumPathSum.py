class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def maxPathSum(self, root):
        m = [0]
        self.helper(root, m)
        return m[0]
        
    def helper(self, root, m):
        if root == None: return 0
        left = max(self.helper(root.left, m), 0)
        right = max(self.helper(root.right, m), 0)
        m[0] = max(m[0], left + right + root.val)
        return root.val + max(left, right)