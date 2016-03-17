#dynamic programming
#Coin Change
coins=[52,480,116,409,170,240,496]
amount = 823000
#coins=[5,2]
#amount=21

class Solution(object):
	def coinChange(self,coins,amount):
		coins.sort(reverse=True)
		self.valid=True
		cache={}
		def dp(coins,diff,valid):
			if diff==0:
				return 0
			elif diff in cache.keys():
				return cache[diff]
			else:
				for i in range(len(coins)):
					if diff-coins[i]<0:
						continue
					elif dp(coins,diff-coins[i],valid)==None:
						self.valid=False
						continue
					else:
						count=dp(coins,diff-coins[i],valid)+1
						cache[diff]=count
						return count
		res=dp(coins,amount,True)
		if self.valid==False or res==None:
			return -1
		else:
			return res


	def coinChange2(self,coins,amount):
		MAX=float('inf')
		res=[0]+[MAX]*(amount)
		for i in range(1,amount+1):
			for c in coins:
				pre=i-c
				if pre<0:
					continue
				elif res[pre]!=-1 and res[i]==MAX:
					res[i]=res[pre]+1
				elif res[pre]==-1:
					continue
				elif res[i]!=MAX:
					res[i]=min(res[i],res[pre]+1)
			if res[i]==MAX:
				res[i]=-1
			#print res
		return res[amount]

	def coinChange3(self,coins,amount):
		pre=[None]*max(coins)
		pre[-1]=0
		for i in range(0,amount):
			cur=[]
			for c in coins:
				if pre[-c]>=0:
					cur.append(pre[-c]+1)
			if len(cur)==0:
				num=-1
			else:
				num=min(cur)
			pre=pre[1:]+[num]
		return num

	def coinChange4(self,coins,amount):
		MAX=float('inf')
		dp=[0]+[MAX]*amount
		for i in xrange(1,amount+1):
			dp[i]=min(dp[i-c] if i-c>=0 else MAX for c in coins)+1
		return [dp[amount],-1][dp[amount]==MAX]

sl=Solution()
print sl.coinChange2(coins,amount)
print sl.coinChange3(coins,amount)
print sl.coinChange4(coins,amount)