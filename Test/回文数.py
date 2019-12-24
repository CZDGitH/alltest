#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif 0 <= x <= 9:
            return True
        elif x % 10 == 0:
            return False
        temp,divide = 0,x
        while(1):
            remainder = divide % 10
            divide = divide // 10
            temp = temp * 10 + remainder
            if divide == temp:
                return True
            elif divide < temp:
                if divide == temp // 10:
                    return True
                else:
                    return False

t =Solution()

s = t.isPalindrome(12321)
print(s)