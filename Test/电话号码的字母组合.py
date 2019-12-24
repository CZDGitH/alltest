#!/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        words = []
        def oneByOne(combinationWords:str,nextDigits:str):
            if len(nextDigits) == 0:
                words.append(combinationWords)
            else:
                for i in phone[nextDigits[0]]:
                    oneByOne(combinationWords + i,nextDigits[1:])
        if digits:
            oneByOne('',digits)
        return words

s = Solution()
digits = "23"
t = s.letterCombinations(digits = digits)
print(t)



