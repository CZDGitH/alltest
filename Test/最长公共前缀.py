#!/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        lValue = len(strs[0])
        removeV =strs[0]
        temp =''
        for i in strs[1::]:
            if len(i) < lValue:
                lValue,removeV = len(i),i
        strs.remove(removeV)
        for j in range(lValue):
            for value in strs:
                if not removeV[j] == value[j]:
                    return temp
            temp += removeV[j]
        return temp

t = Solution()
s = t.longestCommonPrefix([])
print(s)

