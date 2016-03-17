import copy
class Solution(object):
	def maximalSquare(self,matrix):
		rows, max_size = len(matrix), 0
		'''
		size[i]: the current number of continuous '1's in a column of matrix. Reset when discontinued.
		The idea is to do a by-row scan, updating size[i]
		Then check if there are continuous elements in size whose value is bigger than current maximal size.
		'''
		if rows > 0:
			cols = len(matrix[0])
			size = [0] * cols
			for x in xrange(rows):
				# update size
				count, size = 0, map(lambda x, y: x+1 if y == '1' else 0, size, matrix[x])
				for y in xrange(cols):
					# check if it exceeds current maximal size
					if size[y] > max_size:
						count += 1
						if count > max_size:
							# increase maximal size by 1
							max_size += 1
							break
					else:
						count = 0

		return max_size*max_size

	def maximalSquare2(self,matrix):
		rows,max_size=len(matrix),0
		if rows==0:
			return 0
		cols=len(matrix[0])
		tmp=[0]*cols
		res=[0]*cols
		for i in xrange(rows):
			row=matrix[i]
			for j in xrange(cols):
				#element is 0
				if int(row[j])==0:
					res[j]=0
				#element is 1
				elif j==0:
					res[j]=1
				else:
					res[j]=min(int(res[j-1]),int(tmp[j-1]),int(tmp[j]))+1
			tmp=copy.deepcopy(res)
			max_size=max(max_size,max(tmp))
			print tmp
		return max_size**2
sl=Solution()
matrix=[['1','1'],['1','1']]

matrix=[['1','0','0','1','0','1','1','0'],['0','0','1','0','1','1','1','0'],['1','1','1','1','1','1','1','1'],
['0','1','1','1','1','1','1','0'],['1','1','0','0','1','1','1','0'],['1','0','0','0','1','0','0','0']]
matrix=["1101","1101","1111"]

for m in matrix:
	for n in m:
		print n ,
	print ''
print sl.maximalSquare(matrix)
print sl.maximalSquare2(matrix)
