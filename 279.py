import math
cache={}
class Solution(object):
	def numSqaures(self,n):
		square=[]
		MAX=float('inf')
		res=[0]+[MAX]*(n)
		k=0
		for i in xrange(1,n+1):
			if i==(k+1)**2:
				k+=1
				square.append(k**2)
				res[i]=1
			else:
				res[i]=min(res[i-s]+1 for s in square)
					#res[i]=min(res[i],res[i-s]+1)
		return res[n]

	def numSqaures2(self,n):
		MAX=float('inf')
		res=[0]+[MAX]*(n)
		k=0
		for i in xrange(1,n+1):
			if i==(k+1)**2:
				k+=1
				res[i]=1
			else:
				res[i]=min(res[i-k**2]+1 for k in xrange(k+1))
		return res[n]

	def numSqaures3(self,n):
		global cache
		k=int(math.sqrt(n))
		sqrt=[x**2 for x in range(1,k+1)]
		def dp(n):
			if n<0:
				return float('inf')
			if n==0:
				return 0
			if n in cache:
				return cache[n]
			else:
				if n in sqrt:
					res=1
				else:
					res=min([dp(n-s) for s in sqrt])+1
				cache[n]=res
				return res
		return dp(n)

	numSquaresDP = [0]
	def numSquares4(self, n):
		if len(self.numSquaresDP) <= n:
			perfectSqr = [v**2 for v in xrange(1, int(math.sqrt(n)) + 1)]
			for i in xrange(len(self.numSquaresDP), n + 1):
				self.numSquaresDP.append(min(1 + self.numSquaresDP[i - sqr] for sqr in perfectSqr if sqr<=i))
			return self.numSquaresDP[n]  

sl=Solution()
print sl.numSquares4(10350)
print sl.numSqaures2(10350)

