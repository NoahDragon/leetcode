#
# [357] Count Numbers with Unique Digits
#
# https://leetcode.com/problems/count-numbers-with-unique-digits/description/
#
# algorithms
# Medium (46.10%)
# Total Accepted:    44.4K
# Total Submissions: 96.3K
# Testcase Example:  '2'
#
# Given a non-negative integer n, count all numbers with unique digits, x,
# where 0 ≤ x < 10n.
# 
# 
# ⁠   Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range
# of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
# 
# 
# Credits:Special thanks to @memoryless for adding this problem and creating
# all test cases.
#
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
