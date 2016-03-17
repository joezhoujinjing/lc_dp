class Solution(object):
	def maxProfit(self,prices):
		hold=-float('inf')
		cooldown=-float('inf')
		notHold=0
		for p in prices:
			hold,notHold,cooldown=max(hold,notHold-p),max(notHold,cooldown),hold+p
			#print 'p',p,'hold',hold,'not hold',notHold,'cd',cooldown
		return max(notHold,cooldown)

	def maxProfit2(self,prices):
		#state = 0: not hold; 1: hold; 2: cd
		state=0
		hold=float('inf')
		cd=float('inf')
		notHold=0
		for p in prices:
			if state==1:
				#buy or hold
				if notHold-p>hold:
					notHold=notHold-p
					state=1
			elif state==0:
				if cd>notHold:
					notHold=cd
			elif state==2:
				state=0
				cd=hold+p




		return 0
prices=[5,2,9,5,1,10,10,2,5,9]
prices=[1,2,3,0,2]
sl=Solution()
print sl.maxProfit(prices)
print sl.maxProfit2(prices)
