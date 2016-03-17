from Queue import PriorityQueue
class Solution(object):
	pq=PriorityQueue()
	def minPathSum(self,grid):
		self.pq.put((grid[0][0],(0,0)))
		while True:
			cur=self.pq.get()
			curSum=cur[0]
			curPos=cur[1]
			if curPos[0]==len(grid)-1 and curPos[1]==len(grid[0])-1:
				return curSum
			#right side
			else:
				if curPos[1]<len(grid[0])-1:
					rightPos=(curPos[0],curPos[1]+1)
					rightSum=grid[rightPos[0]][rightPos[1]]+curSum
					self.pq.put((rightSum,rightPos))
				#down side
				if curPos[0]<len(grid)-1:
					downPos=(curPos[0]+1,curPos[1])
					downSum=grid[downPos[0]][downPos[1]]+curSum
					self.pq.put((downSum,downPos))


	def minPathSum2(self,grid):
		MAX=float('inf')
		dp=[MAX]*len(grid[0])
		m=len(grid)
		n=len(grid[0])
		dp[0]=grid[0][0]
		for i in range(m):
			for j in range(n):
				if i==0 and j!=0:
					dp[j]=dp[j-1]+grid[0][j]
				elif i!=0:
					if j==0:
						dp[j]=dp[j]+grid[i][0]
					else:
						dp[j]=min(dp[j],dp[j-1])+grid[i][j]
		return dp[n-1]


sl=Solution()
grid=[[2,1,9,4],[0,1,1,2],[10,1,3,5],[7,1,5,4]]
#grid=[[1,2],[5,6],[1,1]]
print sl.minPathSum(grid)
print sl.minPathSum2(grid)