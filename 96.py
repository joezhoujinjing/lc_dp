class Solution(object):
	def numTrees(self,n):
		self.cache={}
		def dp(n):
			if n in self.cache:
				return self.cache[n]
			if n<=1:
				return 1
			res=0
			for i in range(1,n+1):
				res+=dp(i-1)*dp(n-i) 
			self.cache[n]=res
			return res
		return dp(n)
sl=Solution()
print sl.numTrees(13)