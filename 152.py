class Solution(object):
	def maxProduct(self,nums):
		localMax=nums[0]
		localMin=nums[0]
		MAX=float('-inf')
		for i in range(1,len(nums)):
			pre=(localMax,localMin)
			localMax=max(nums[i],pre[0]*nums[i],pre[1]*nums[i])
			localMin=min(nums[i],pre[0]*nums[i],pre[1]*nums[i])
			MAX=max(localMax,MAX)
		return MAX

sl=Solution()
nums=[-2,1,-2,4,3,5,6,1,5]
nums=[-2,1,-3,4,-1,2,1,-5,-4]
print sl.maxProduct(nums)