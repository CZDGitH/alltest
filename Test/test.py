#!/usr/bin/python3
# -*- coding: utf-8 -*-
height = [1,2,3]
print(height[1::])
dict1 = {1000:'M', 900:'CM',500:'D',400:'CD',100:'C',
         90:'XC',50:'L',40:'XL',10:'X',
         9:'IX',5:'V',4:'IV',1:'I'}
print(dict1)
for k in dict1:
    print(k)
    print(dict1[k])

s = 'CM'
print(s[0:2])

strs = ['1','2','3']
strs.remove('1')
for i in strs:
    print(i)
print('-------------------')
phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

print(phone['2'])
nums = [1,2,3,4]
nums.remove(1)
print(nums)
s = 'abc'
s = s[0:1]+s[2:]

print('({}){}'.format('', '()'))
print(len([None,None,None]))
print('----------------')
temp = [1,1,1,2]
temp.remove(1)
print(temp)