#
# [612] Shortest Distance in a Plane
#
# https://leetcode.com/problems/shortest-distance-in-a-plane/description/
#
# database
# Medium (52.42%)
# Total Accepted:    1.9K
# Total Submissions: 3.6K
# Testcase Example:  '{"headers":{"point_2d":["x","y"]},"rows":{"point_2d":[[-1,-1],[0,0],[-1,-2]]}}'
#
# Table point_2d holds the coordinates (x,y) of some unique points (more than
# two) in a plane.
# Write a query to find the shortest distance between these points rounded to
# 2 decimals.
# ⁠
# 
# | x  | y  |
# |----|----|
# | -1 | -1 |
# | 0  | 0  |
# | -1 | -2 |
# 
# ⁠
# The shortest distance is 1.00 from point (-1,-1) to (-1,2). So the output
# should be:
# 
# | shortest |
# |----------|
# | 1.00     |
# 
# ⁠
# Note: The longest distance among all the points are less than 10000.
#
# Write your MySQL query statement below
