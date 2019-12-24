#!/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if len(nums) < 3: return ''
        temp = []
        for l in range(len(nums) - 2):
            if nums[l] > 0:break
            elif (l > 0 and nums[l] == nums[l - 1]):continue
            i,j = l + 1,len(nums) - 1
            while i < j:
                s = nums[l] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:j -= 1
                else:
                    temp.append([nums[l],nums[i],nums[j]])
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return temp

s = Solution()
nums = [-2,0,1,1,2]
t = s.threeSum(nums)
print(t)
