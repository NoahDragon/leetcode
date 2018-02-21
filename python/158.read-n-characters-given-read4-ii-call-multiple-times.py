#
# [158] Read N Characters Given Read4 II - Call multiple times
#
# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/description/
#
# algorithms
# Hard (24.75%)
# Total Accepted:    38.2K
# Total Submissions: 154.3K
# Testcase Example:  '""\n[read(0)]'
#
# 
# The API: int read4(char *buf) reads 4 characters at a time from a file.
# 
# 
# 
# The return value is the actual number of characters read. For example, it
# returns 3 if there is only 3 characters left in the file.
# 
# 
# 
# By using the read4 API, implement the function int read(char *buf, int n)
# that reads n characters from the file.
# 
# 
# 
# Note:
# The read function may be called multiple times.
# 
#
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        
