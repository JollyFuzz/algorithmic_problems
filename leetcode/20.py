# https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_pairs = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []
        for bracket in s:
            if stack and bracket in bracket_pairs:
                if bracket_pairs[bracket] == stack[-1]:
                    stack.pop(-1)
                else:
                    stack.append(bracket)
            else:
                stack.append(bracket)
        return len(stack) == 0


# case1 = "()[]{}"
case2 = "()[]{{}"
Solution().isValid(case2)