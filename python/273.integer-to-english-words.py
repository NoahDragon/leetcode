#
# [273] Integer to English Words
#
# https://leetcode.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (22.70%)
# Total Accepted:    54.7K
# Total Submissions: 240.9K
# Testcase Example:  '123'
#
# 
# Convert a non-negative integer to its english words representation. Given
# input is guaranteed to be less than 231 - 1.
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
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
