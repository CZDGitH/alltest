#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Solution:
    def reverse(self, x: int) -> int:
        y,backNum = abs(x),0
        loca = (1<<31) - 1 if x > 0 else 1<<31
        while(y > 0):
            pop = y % 10
            y = y // 10
            backNum = backNum * 10 +pop
            if backNum > loca:
                return 0
        return backNum if x > 0 else -backNum

t = Solution()
back = t.reverse(-1563847412)
print(back)

