#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (41.78%)
# Total Accepted:    143.4K
# Total Submissions: 343.2K
# Testcase Example:  '1'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1...n?
# 
# 
# For example,
# Given n = 3, there are a total of 5 unique BST's.
# 
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
#
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
