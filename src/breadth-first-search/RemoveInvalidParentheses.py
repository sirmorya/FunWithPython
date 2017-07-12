class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        queue = [s]
        result = []
        if s == None:
            return result
        found = False
        visited = []
        while(len(queue) != 0):
           str = queue.pop(0)
           if self.isValid(str):
               result.append(str)
               found = True
           if found:
               continue
           for i in range(0, len(str)):
               if s[i] != '(' or s[i] != ')':
                   continue
               t = s[0:i] + s[i + 1:len(s)]
               if t not in visited:
                   queue.append(t)
                   visited.append(t)
        
        
	def isValid(self, s):
		c = 0
		for i in range(0, len(s)):
			if s[i] == '(':
				c = c + 1
			elif s[i] == ')' :
                c = c - 1
        return c == 0
