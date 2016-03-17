class NumArray(object):
	def __init__(self,nums):
		for i in range(1,len(nums)):
			nums[i]=nums[i]+nums[i-1]

	def sumRange(self,i ,j):
		if i ==0:
			return nums[j]
		else:
			return nums[j]-nums[i-1]
nums=[-2,0,3,-5,2,-1]
numArray=NumArray(nums)
numArray.sumRange(2,5)
