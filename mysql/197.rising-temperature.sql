#
# [197] Rising Temperature
#
# https://leetcode.com/problems/rising-temperature/description/
#
# database
# Easy (30.53%)
# Total Accepted:    42.5K
# Total Submissions: 139.3K
# Testcase Example:  '{"headers": {"Weather": ["Id", "Date", "Temperature"]}, "rows": {"Weather": [[1, "2015-01-01", 10], [2, "2015-01-02", 25], [3, "2015-01-03", 20], [4, "2015-01-04", 30]]}}'
#
# Given a Weather table, write a SQL query to find all dates' Ids with higher
# temperature compared to its previous (yesterday's) dates.
# 
# 
# +---------+------------+------------------+
# | Id(INT) | Date(DATE) | Temperature(INT) |
# +---------+------------+------------------+
# |       1 | 2015-01-01 |               10 |
# |       2 | 2015-01-02 |               25 |
# |       3 | 2015-01-03 |               20 |
# |       4 | 2015-01-04 |               30 |
# +---------+------------+------------------+
# 
# 
# For example, return the following Ids for the above Weather table:
# 
# +----+
# | Id |
# +----+
# |  2 |
# |  4 |
# +----+
# 
#
# Write your MySQL query statement below

