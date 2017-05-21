class HelloClass(object):
    def helloMethod(self, node):
        print('hello world in method ' + str(node.val))
        
class TreeNode(object):
    def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None
      
node = TreeNode(5)
HelloClass().helloMethod(node)