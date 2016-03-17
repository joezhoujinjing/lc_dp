


class Solution(object):
	def lengthOFLIS(self,nums):
		if len(nums)==0:
			return 0
		res=[1]*len(nums)
		for i in range(1,len(nums)):
			tmp=[1]
			tmp=[res[j]+1 for j in range(i) if nums[j]<nums[i]]+[1]
			res[i]=max(tmp)
		return max(res)

sl=Solution()
print sl.lengthOFLIS([])
print sl.lengthOFLIS([-1,3,2,1,9,3,5,9])
print sl.lengthOFLIS([1,0,-1])