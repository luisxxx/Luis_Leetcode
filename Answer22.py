class Solution:
    # @param an integer
    # @return a list of string
	def generateParenthesis(self, n):
		result = []
		current = ''
		self.generateParenthesisrecu(n,n,current,result)
		return result
	
	def generateParenthesisrecu(self,left,right,current,result):
		if left ==0 & right == 0:
			result.append(current)
		else:
			if left>0:
				self.generateParenthesisrecu(left-1,right,current+'(',result)
			if right > left:
				self.generateParenthesisrecu(left,right-1,current+')',result)
	
		

if __name__ == "__main__":
    print Solution().generateParenthesis(4)