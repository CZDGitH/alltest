#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(','}':'{',']':'['}
        temp = []
        for i in s:
            if i in mapping:
                pop = temp.pop() if temp else '#'
                if pop != mapping[i]:
                    return False
            else:
                temp.append(i)
        return not temp

s = Solution()
l = "]"
t = s.isValid(l)
print(t)


