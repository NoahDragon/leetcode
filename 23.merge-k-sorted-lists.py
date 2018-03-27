# Question:
#	Merge k sorted linked lists and return it as one sorted list. 
#	Analyze and describe its complexity.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def link2List(l):
            if l is None:
                return []
            
            result = []
            
            while not (l is None):
                result.append(l.val)
                l = l.next
                
            return result
        
        r = []
        
        for l in lists:
            r.extend(link2List(l))

        return sorted(r)