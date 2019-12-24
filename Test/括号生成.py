#!/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = []
        def addSign(s: str,num: int,leftcount: int,rightcount:int,n: int):
            if rightcount < n:
                if num == 0 and leftcount < n:
                    addSign(s + '(',num + 1,leftcount + 1,rightcount,n)
                elif 0 < num < n:
                    if leftcount < n:
                        addSign(s + '(',num + 1,leftcount + 1,rightcount,n)
                    addSign(s + ')',num - 1,leftcount,rightcount + 1,n)
                else:
                    addSign(s + ')', num - 1, leftcount,rightcount + 1, n)
            else:
                temp.append(s)
        if n > 0:
            addSign('',0,0,0,n)
        return temp
s = Solution()
g = s.generateParenthesis(3)
print(g)


