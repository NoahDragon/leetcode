#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (42.23%)
# Total Accepted:    102.1K
# Total Submissions: 241.8K
# Testcase Example:  '[]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# 
# 
# For example:
# Given the following binary tree,
# 
# ⁠  1            
# 
# 
# You should return [1, 3, 4].
# 
# 
# Credits:Special thanks to @amrsaqr for adding this problem and creating all
# test cases.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
