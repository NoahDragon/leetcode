#
# [273] Integer to English Words
#
# https://leetcode.com/problems/integer-to-english-words
#
# Hard (21.92%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '123'
#
# 
# Convert a non-negative integer to its english words representation. Given
# input is guaranteed to be less than 2^31 - 1.
# 
# 
# For example,
# 
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
#
class Solution(object):
	recursiveCount = 0

	scale = {
		1: '',
		2: 'Thousand',
		3: 'Million',
		4: 'Billion',
		5: 'Trillion'
	}

	tenToTwentySwitcher = {
		0: 'Ten',
		1: 'Eleven',
		2: 'Twelve',
		3: 'Thirteen',
		4: 'Fourteen',
		5: 'Fifteen',
		6: 'Sixteen',
		7: 'Seventeen',
		8: 'Eighteen',
		9: 'Nineteen'
	}

	twentyToHundredSwitcher = {
		0: '',
		2: 'Twenty',
		3: 'Thirty',
		4: 'Forty',
		5: 'Fifty',
		6: 'Sixty',
		7: 'Seventy',
		8: 'Eighty',
		9: 'Ninety'
	}

	digitToWordSwitcher = {
		0: 'Zero',
		1: 'One',
		2: 'Two',
		3: 'Three',
		4: 'Four',
		5: 'Five',
		6: 'Six',
		7: 'Seven',
		8: 'Eight',
		9: 'Nine'
	}

	def digitToWord(self, digitsOfThree):
		"""
		:type digitsOfThree: array int
		:rtype: str
		"""
		self.recursiveCount += 1
		d3 = digitsOfThree[(self.recursiveCount-1)*3:self.recursiveCount*3]
		returnStr = []

		if len(d3) == 0:
			return returnStr

		if len(d3) == 1:
			returnStr.append(self.digitToWordSwitcher[d3[0]])
		if len(d3) >= 2: 
			if d3[1] == 1:
				returnStr.append(self.tenToTwentySwitcher[d3[0]])
			elif d3[0] == 0 and d3[1] == 0:
				returnStr = []
			else:
				if d3[0] != 0:
					returnStr.append(self.digitToWordSwitcher[d3[0]])
				if d3[1] != 0:
					returnStr.append(self.twentyToHundredSwitcher[d3[1]])
		
		if len(d3) == 3:
			if d3[2] != 0:
				returnStr.append('Hundred')
				returnStr.append(self.digitToWordSwitcher[d3[2]])
		
		returnStr.insert(0, self.scale[self.recursiveCount])

		if len(d3) == 3 and d3[0] == 0 and d3[1] == 0 and d3[2] == 0:
			returnStr = []

		return returnStr + self.digitToWord(digitsOfThree) 

	def numberToWords(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		digits = map(lambda c: int(c), list(str(num)))

		result = self.digitToWord(digits[::-1])[::-1]
		return " ".join(result).strip()
