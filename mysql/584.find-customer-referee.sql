#
# [584] Find Customer Referee
#
# https://leetcode.com/problems/find-customer-referee/description/
#
# database
# Easy (61.69%)
# Total Accepted:    3.5K
# Total Submissions: 5.6K
# Testcase Example:  '{ "headers": { "customer": [ "id", "name", "referee_id"] }, "rows": {"customer": [[1, "Will", null], [2, "Jane", null], [3, "Alex", 2], [4, "Bill", null], [5, "Zack", 1], [6, "Mark", 2]]}}'
#
# Given a table customer holding customers information and the referee.
# 
# 
# +------+------+-----------+
# | id   | name | referee_id|
# +------+------+-----------+
# |    1 | Will |      NULL |
# |    2 | Jane |      NULL |
# |    3 | Alex |         2 |
# |    4 | Bill |      NULL |
# |    5 | Zack |         1 |
# |    6 | Mark |         2 |
# +------+------+-----------+
# 
# 
# Write a query to return the list of customers NOT referred by the person with
# id '2'.
# 
# For the sample data above, the result is:
# 
# +------+
# | name |
# +------+
# | Will |
# | Jane |
# | Bill |
# | Zack |
# +------+
# 
#
# Write your MySQL query statement below
