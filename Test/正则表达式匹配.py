#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # print(re.match(p,s))
        # temp = re.match(p,s)
        # return False if temp is None else len(temp.group()) == len(s)
        memo = {}
        def dp(i,j):
            if (i,j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {'.',s[i]}
                    if j + 1 < len(p)    and p[j + 1] == '*':
                        ans = dp(i,j + 2) or first_match and dp(i + 1,j)
                    else:
                        ans = first_match and dp(i + 1,j + 1)
                memo[i,j] = ans
            return memo[i,j]
        return dp(0,0)



t = Solution()
s = "abcd"
p = ".*c"
back = t.isMatch(s,p)
print(back)
