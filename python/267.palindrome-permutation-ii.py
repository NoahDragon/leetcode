#
# [267] Palindrome Permutation II
#
# https://leetcode.com/problems/palindrome-permutation-ii/description/
#
# algorithms
# Medium (32.12%)
# Total Accepted:    17.1K
# Total Submissions: 53.3K
# Testcase Example:  '"aabb"'
#
# 
# Given a string s, return all the palindromic permutations (without
# duplicates) of it. Return an empty list if no palindromic permutation could
# be form.
# 
# 
# For example:
# 
# 
# Given s = "aabb", return ["abba", "baab"].
# 
# 
# Given s = "abc", return [].
# 
#
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
