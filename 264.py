from Queue import PriorityQueue
class Solution(object):
	#prime factors only include 2,3,5. first 10 1,2,3,4,5,6,8,9,10,12
	def nthUglyNumber(self,n):
		unglyNumber=[1]
		candidates=[2,3,5]
		while len(unglyNumber)<n:
			candy=min(candidates)
			if candy!=unglyNumber[-1]:
				candidates.remove(candy)
				candidates+=candy*2,candy*3,candy*5
				unglyNumber.append(candy)
			else:
				candidates.remove(candy)
		return unglyNumber[-1]
	def nthUglyNumber2(self,n):
		pq=PriorityQueue()
		uglyNumber=[-1]*n
		pq.put(1)
		i=0
		while i<n:
			candy=pq.get()
			if len(uglyNumber)==0 or candy!=uglyNumber[i-1]:
				uglyNumber[i]=candy
				pq.put(candy*2)
				pq.put(candy*3)
				pq.put(candy*5)
				i+=1
		return uglyNumber[-1]
	def nthUglyNumber3(self,n):
		ugly=[1]*n
		i2=i3=i5=-1
		x=v2=v3=v5=1
		for k in xrange(n):
			x=min(v2,v3,v5)
			ugly[k]=x
			if x==v2:
				i2+=1
				v2=ugly[i2]*2
			if x==v3:
				i3+=1
				v3=ugly[i3]*3
			if x==v5:
				i5+=1
				v5=ugly[i5]*5
			print i2,i3,i5
			print v2,v3,v5
			print ugly
		return x

sl=Solution()
print sl.nthUglyNumber3(10)
'''
print sl.nthUglyNumber(10000)
print sl.nthUglyNumber2(10000)
print sl.nthUglyNumber3(10000)
'''