#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (23.20%)
# Total Accepted:    118.1K
# Total Submissions: 509.2K
# Testcase Example:  '""'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# 
# For "(()", the longest valid parentheses substring is "()", which has length
# = 2.
# 
# 
# Another example is ")()())", where the longest valid parentheses substring is
# "()()", which has length = 4.
# 
#
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
