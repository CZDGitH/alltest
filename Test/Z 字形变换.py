#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lenS = len(s)
        local = 0
        tempS = ['']*numRows
        while local < lenS:
            if numRows == 1:
                tempS[0] = s
                break
            for i in range(numRows - 1):
                if local >= lenS:
                    break
                tempS[i] += s[local]
                local += 1
            for j in range(numRows - 1,0,-1):
                if local >= lenS:
                    break
                tempS[j] += s[local]
                local += 1
        backS = ''.join(tempS)
        return backS


t = Solution()
backS = t.convert(s = 'A',numRows=1)
print(backS)