#
# [248] Strobogrammatic Number III
#
# https://leetcode.com/problems/strobogrammatic-number-iii/description/
#
# algorithms
# Hard (32.50%)
# Total Accepted:    11.1K
# Total Submissions: 34.3K
# Testcase Example:  '"0"\n"0"'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# Write a function to count the total strobogrammatic numbers that exist in the
# range of low 
# For example,
# Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three
# strobogrammatic numbers.
# 
# 
# Note:
# Because the range might be a large number, the low and high numbers are
# represented as string.
# 
#
class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        
