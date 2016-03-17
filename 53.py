class Solution(object):
	def maxSubArray(self,nums):
		res=[nums[0]]+[None]*(len(nums)-1)
		for i in range(1,len(nums)):
			if res[i-1]+nums[i]<nums[i]:
				res[i]=nums[i]
			else:
				res[i]=res[i-1]+nums[i]
		print res
		return max(res)


sl=Solution()
nums=[-2,1,-3,4,-1,2,1,-5,4]
print sl.maxSubArray(nums)