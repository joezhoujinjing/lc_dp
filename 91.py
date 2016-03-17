class Solution(object):
	def numDecodings(self,s):
		if not len(s) or s[0]=='0':
			return 0
		cache={}
		cache[0]=1
		cache[1]=1
		def dp(n):
			if n in cache:
				return cache[n]
			elif n<0:
				return 0
			else:
				return dp(n-1)+dp(n-2)
		res=1
		start=0
		for i in range(0,len(s)):
			if s[i]=='0':
				if not s[i-1] in '12':
					return 0
				res*=dp(i-2-start+1)
				start=i+1
			elif s[i] not in '12' or i==len(s)-1:
				if i>0:
					if int(s[i-1:i+1])<27 and s[i-1]!='0':
						res*=dp(i-start+1)
						start=i+1
					elif int(s[i-1:i+1])>=27 and s[i-1]!='0':
						res*=dp(i-start)
						start=i+1
					else:
						start=i+1
				elif i==0:
					start=i+1
		return res

	def numDecodings1(self,s):
		if not len(s) or s[0]=='0':
			return 0
		cache={}
		cache[0]=1
		cache[1]=1
		def dp(n):
			if n in cache:
				return cache[n]
			elif n<0:
				return 0
			else:
				return dp(n-1)+dp(n-2)
		res=1
		start=0
		for i in range(0,len(s)):
			if s[i]=='0':
				if not s[i-1] in '12':
					return 0
				res*=dp(i-2-start+1)
				start=i+1
			elif s[i] not in '12' or i==len(s)-1:
				if i==0:
					start=i+1
				elif s[i-1]=='0':
					start=i+1
				elif int(s[i-1:i+1])<27:
					res*=dp(i-start+1)
					start=i+1
				elif int(s[i-1:i+1])>=27:
					res*=dp(i-start)
					start=i+1
		return res

	def numDecodings2(self,s):				
		if not len(s) or s[0]=='0':
			return 0
		total=1
		pre=1
		for i in range(1,len(s)):
			if s[i]=='0':
				if not s[i-1] in '12':
					return 0
				total = pre
				continue
			elif int(s[i-1:i+1])<27 and s[i-1]!='0':
				pre,total=total,total+pre
			else:
				pre=total

		return total

sl=Solution()
#print sl.numDecodings('1234334')

print sl.numDecodings('232092323209232320923')
print sl.numDecodings('12')
print sl.numDecodings('100')
print sl.numDecodings('27')
print sl.numDecodings('99')
print sl.numDecodings('31')
print sl.numDecodings('611')
print sl.numDecodings1('232092323209232320923')
print sl.numDecodings1('12')
print sl.numDecodings1('100')
print sl.numDecodings1('27')
print sl.numDecodings1('99')
print sl.numDecodings1('31')
print sl.numDecodings1('611')
