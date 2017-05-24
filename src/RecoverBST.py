class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    pre = None
    first = None
    second = None
    def recoverTree(self, root):

        self.inorder(root)
        if self.first != None and self.second != None:
            val = self.first.val
            self.first.val = self.second.val
            self.second.val = val
        
    def inorder(self, root):
        if root == None: return
        self.inorder(root.left)
        
        if self.pre == None:
            self.pre = root
        else:
            if root.val < self.pre.val:
                if self.first == None:
                    self.first = self.pre
                self.second = root
            self.pre = root
            
        self.inorder(root.right)
            