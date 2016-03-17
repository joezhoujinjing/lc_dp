#Triangle
import copy

class Solution(object):
	def minimumTotal(self,triangle):
		res=[]
		MAX=len(triangle[len(triangle)-1])
		tmp=[None]*MAX
		for row in triangle:
			print 'row',row
			if len(res)==0:
				res=copy.deepcopy(row)
			else:
				for i in range(len(row)):
					#print row,res,i
					if i ==0:
						tmp[i]=res[i]+row[i]
					elif i==len(row)-1:
						tmp[i]=res[i-1]+row[i]
					else:
						tmp[i]=min(res[i-1],res[i])+row[i]
				res=copy.deepcopy(tmp)
			print 'res',res
		return min(res)

	def minimumTotal2(self,triangle):
		pre=[]
		res=[]
		res=triangle[0]
		rowNum=len(triangle)

		for i in range(1,rowNum):
			row=triangle[i]
			pre=copy.deepcopy(res)
			res[0]=pre[0]+row[0]
			for j in range(1,len(row)-1):
				res[j]=min(pre[j-1],pre[j])+row[j]
			res.append(pre[len(row)-2]+row[len(row)-1])
			print res
		return min(res)

sl=Solution()
triangle=[[2],[3,4],[6,5,7],[4,1,8,3]]
print sl.minimumTotal(triangle)
print sl.minimumTotal2(triangle)