#
# [8] String to Integer (atoi)
#
# https://leetcode.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (13.95%)
# Total Accepted:    212.6K
# Total Submissions: 1.5M
# Testcase Example:  '""'
#
# Implement atoi to convert a string to an integer.
# 
# Hint: Carefully consider all possible input cases. If you want a challenge,
# please do not see below and ask yourself what are the possible input cases.
# 
# Notes: It is intended for this problem to be specified vaguely (ie, no given
# input specs). You are responsible to gather all the input requirements up
# front.
# 
# 
# 
# Requirements for atoi:
# 
# The function first discards as many whitespace characters as necessary until
# the first non-whitespace character is found. Then, starting from this
# character, takes an optional initial plus or minus sign followed by as many
# numerical digits as possible, and interprets them as a numerical value.
# 
# The string can contain additional characters after those that form the
# integral number, which are ignored and have no effect on the behavior of this
# function.
# 
# If the first sequence of non-whitespace characters in str is not a valid
# integral number, or if no such sequence exists because either str is empty or
# it contains only whitespace characters, no conversion is performed.
# 
# If no valid conversion could be performed, a zero value is returned. If the
# correct value is out of the range of representable values, INT_MAX
# (2147483647) or INT_MIN (-2147483648) is returned.
#
# Note:
#   Really ugly solution, but works... 
#
class Solution:
    def myAtoi(self, strs):
        """
        :type str: str
        :rtype: int
        """
        s = strs.strip().split()
        if not s:
            return 0
        s = list(reversed(list(s[0])))
        result = 0
        sign = 1
        deduct = 0 # use to skip unknown chars
        for i, v in enumerate(s):
            d = None
            if v == '0':
                d = 0
            elif v == '1':
                d = 1
            elif v == '2':
                d = 2
            elif v == '3':
                d = 3
            elif v == '4':
                d = 4
            elif v == '5':
                d = 5
            elif v == '6':
                d = 6
            elif v == '7':
                d = 7
            elif v == '8':
                d = 8
            elif v == '9':
                d = 9
            elif i == len(s) - 1 and v == '-':
                d = 0
                sign = -1
            elif i == len(s) - 1 and v == '+':
                d = 0
                sign = 1
            else:
                result = 0
                deduct += ((i - deduct) + 1)
                continue
            result = sign * (result + d * (10**(i-deduct)))
        if result >  2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        return result
