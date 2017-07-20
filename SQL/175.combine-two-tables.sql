#
# [175] Combine Two Tables
#
# https://leetcode.com/problems/combine-two-tables
#
# database
# Easy (35.32%)
# Total Accepted:    53.5K
# Total Submissions: 151.6K
# Testcase Example:  '{"headers": {"Person": ["PersonId", "LastName", "FirstName"], "Address": ["AddressId", "PersonId", "City", "State"]}, "rows": {"Person": [[1, "Wang", "Allen"]], "Address": [[1, 2, "New York City", "New York"]]}}'
#
# 
# Table: Person
# 
# 
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | PersonId    | int     |
# | FirstName   | varchar |
# | LastName    | varchar |
# +-------------+---------+
# PersonId is the primary key column for this table.
# 
# 
# 
# Table: Address
# 
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | AddressId   | int     |
# | PersonId    | int     |
# | City        | varchar |
# | State       | varchar |
# +-------------+---------+
# AddressId is the primary key column for this table.
# 
# 
# 
# 
# Write a SQL query for a report that provides the following information for 
# each person in the Person table, regardless if there is an address for each 
# of those people:
# 
# 
# 
# FirstName, LastName, City, State
# 
#
# Write your MySQL query statement below

