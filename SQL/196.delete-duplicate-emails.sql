#
# [196] Delete Duplicate Emails
#
# https://leetcode.com/problems/delete-duplicate-emails
#
# database
# Easy (20.19%)
# Total Accepted:    27.7K
# Total Submissions: 137.4K
# Testcase Example:  '{"headers": {"Person": ["Id", "Email"]}, "rows": {"Person": [[1, "john@example.com"], [2, "bob@example.com"], [3, "john@example.com"]]}}'
#
# 
# Write a SQL query to delete all duplicate email entries in a table named
# Person, keeping only unique emails based on its smallest Id.
# 
# 
# +----+------------------+
# | Id | Email            |
# +----+------------------+
# | 1  | john@example.com |
# | 2  | bob@example.com  |
# | 3  | john@example.com |
# +----+------------------+
# Id is the primary key column for this table.
# 
# 
# For example, after running your query, the above Person table should have the
# following rows:
# 
# +----+------------------+
# | Id | Email            |
# +----+------------------+
# | 1  | john@example.com |
# | 2  | bob@example.com  |
# +----+------------------+
# 
#
# Write your MySQL query statement below
