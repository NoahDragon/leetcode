#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (28.20%)
# Total Accepted:    110.2K
# Total Submissions: 390.7K
# Testcase Example:  '["18"]'
#
# 
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# 
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
# 
# 
# 
# Some examples:
# 
# ⁠ ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
# ⁠ ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
# 
# 
#
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
