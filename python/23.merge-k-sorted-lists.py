#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (28.02%)
# Total Accepted:    203.4K
# Total Submissions: 726.1K
# Testcase Example:  '[]'
#
# 
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
