class Solution(object):
	def maxProfit(self,prices):
		if len(prices)==0:
			return 0
		max_profit=0
		min_price=float('inf')
		for price in prices:
			min_price=min(min_price,price)
			profit=price-min_price
			max_profit=max(max_profit,profit)
		return max_profit


prices=[1,4,2,3,1,5,6,4,45,2,3,4,23,5,3]
sl=Solution()
print sl.maxProfit(prices)
