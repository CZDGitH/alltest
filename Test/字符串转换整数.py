# !/usr/bin/python3
# -*- coding: utf-8 -*-
# class Solution:
#     def myAtoi(self, str: str) -> int:
#         strLen = len(str)
#         if strLen == 0:
#             return 0
#         temp = ''
#         for i in range(strLen):
#             if str[i] == ' ' and len(temp) == 0:
#                 continue
#             elif '0' <= str[i] <= '9':
#                 temp += str[i]
#             elif str[i] == '-' or str[i] == '+':
#                 if i < strLen - 1:
#                     if len(temp) == 0 and '0' <= str[i + 1] <= '9':
#                         temp += str[i]
#                     elif len(temp) == 1:
#                         return 0
#                     else:
#                         break
#             elif len(temp) == 0:
#                 return 0
#             else:
#                 break
#         if len(temp) == 0:
#             return 0
#         intTemp = int(temp)
#         if intTemp < -(1 << 31):
#             return -(1 << 31)
#         if intTemp > (1 << 31) - 1:
#             return (1 << 31) - 1
#         return intTemp
import re
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)


print(*re.findall('^[\+\-]?\d+', '+8'.lstrip()))

t = Solution()
s = t.myAtoi("+8")
print(s)
print(-(1<<31))
kwargs = {"data3": "one", "data2": 2, "data1": 3}
print(kwargs)
print(**kwargs)