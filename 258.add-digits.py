#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits
#
# Easy (50.97%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '0'
#
# 
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit. 
# 
# 
# 
# For example:
# 
# 
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only
# one digit, return it.
# 
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
	#
	# The logic is following:
	# for number < 10, then it's expected result;
	# for number >= 10 but <= 99, the maximum digit sum is 18 = 9 + 9
	# so on and so forth, a sum of digit = 99 means a number = 99,999,999,999
	# therefore do the reduce twice could cover the number range from 0 to 1 * 10^11
	# however, add an extra reduce function just for safer, the number could be from 0 to 1 * 10^111
	# which could covers the most number in computers.
	#
	# This solution is brutual and not beautiful, but simple.
	#
	return reduce(lambda x,y: x+y, map(lambda c: int(c), list(str(reduce(lambda x,y: x+y, map(lambda c: int(c), list(str(reduce(lambda x,y: x+y, map(lambda c: int(c), list(str(num))))))))))))
        
