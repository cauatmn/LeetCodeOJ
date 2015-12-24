#Given a string, find the length of the longest substring without repeating characters. For example, the longest #substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest #substring is "b", with the length of 1.
#Subscribe to see which companies asked this question

class Solution(object):
	def lengthOfLongestSubstring(self,s):
		"""
		:type s :str
		:rtype: int
		"""
		maxlen = 1
		currentLen = 1 
		lens = len(s)
		L1 = []
		if s == "":
			return 0
		for i in range(lens):
			for s in range(1,lens):
				if L[i] == L[s]:
					
		print len(L1)
					
			
			
		
			

if __name__ == "__main__":
	L = "12312321"
	Test = Solution()
	Test.lengthOfLongestSubstring(L)
	
	