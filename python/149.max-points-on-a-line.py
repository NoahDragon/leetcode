#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (15.20%)
# Total Accepted:    89.8K
# Total Submissions: 590.8K
# Testcase Example:  '[]'
#
# Given n points on a 2D plane, find the maximum number of points that lie on
# the same straight line.
#
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        
