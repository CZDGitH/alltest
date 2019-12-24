#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Solution:
    def romanToInt(self, s: str) -> int:
        sLen = len(s)
        dict1 = {'M':1000, 'CM':900, 'D':500, 'CD':400,'C':100,
                 'XC':90,'L':50,  'XL':40,  'X':10,
                  'IX':9, 'V':5, 'IV':4,'I':1}
        temp = 0
        i = 0
        while i < sLen:
            if s[i:i+2] in ('CM','CD','XC','XL','IX','IV'):
                temp += dict1[s[i:i+2]]
                i += 2
            else:
                temp += dict1[s[i]]
                i += 1
        return temp

t = Solution()
s = t.romanToInt('IV')
print(s)