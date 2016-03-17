nums=[1,2,3,4,5]

res=[]
def subsets(nums):
	nums.sort()
	for i in range(0,len(nums)):
		if len(nums)>0:
			newNums=nums[0:i]+nums[i+1:len(nums)]
			res.append(nums)
			subsets(newNums)

#subsets(nums)
res.sort()
for i in range(len(res)-1,0,-1):
	if res[i]==res[i-1]:
		res.remove(res[i])

def subsets2(nums):
	nums.sort()
	ans,stack,x,n=[[]],[],0,len(nums)
	while True:
		if x<n:
			stack+=[(x,nums[x])]
			ans+=[zip(*stack)[1]]
			x+=1
			print 'stack'
			print stack,x
		elif stack:
			x=stack.pop()[0]+1
		else:
			return ans
#print subsets2(nums)

def subsets3(nums):
	if len(nums)==0:
		return [[]]
	nums.sort()
	without_1st = subsets3(nums[1:]) 
	with_1st = [([nums[0]]+x) for x in without_1st]
	return without_1st+with_1st
#print subsets3(nums)

def trial(nums):
	if len(nums)==0:
		return [[]]
	no_1st=trial(nums[1:])
	yes_1st=[([nums[0]]+x) for x in no_1st]
	return no_1st+yes_1st
print trial(nums)
