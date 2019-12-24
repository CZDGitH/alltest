#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Solution:
    def intToRoman(self, num: int) -> str:
        dict1 = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
                 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        temp = ''
        for key in dict1:
            lKey = num // key
            num %= key
            for i in range(lKey):
                temp += dict1[key]
        return temp
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         ge = num % 10
#         shi = num//10%10
#         bai = num//100%10
#         qian = num//1000
#         str_ge = self.judge(ge,"I","V","X")
#         str_shi = self.judge(shi,"X","L","C")
#         str_bai = self.judge(bai,"C","D","M")
#         str_qian = self.judge(qian,rm1 = "M")
#         return str_qian+str_bai+str_shi+str_ge
#     def judge(self,num=0,rm1="",rm2="",rm3=""):
#         if num<=3:
#             return num*rm1
#         elif num == 4:
#             return rm1+rm2
#         elif num<=8:
#             return rm2+rm1*(num-5)
#         else:
#             return rm1+rm3

t = Solution()
s = t.intToRoman(3)
print(s)