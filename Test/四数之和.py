#!/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        if len(nums) < 4:return ''
        temp = []
        for l in range(len(nums) - 3):
            if target >= 0 and nums[l] > target:break
            elif (l > 0 and nums[l] == nums[l - 1]):continue
            for h in range(len(nums) - 1,l + 2,-1):
                if target <= 0 and nums[h] < target:break
                elif (h < len(nums) - 1 and nums[h] == nums[h + 1]):continue
                i, j = l + 1, h - 1
                while i < j:
                    s = nums[l] + nums[i] + nums[j] + nums[h]
                    if s < target:
                        i += 1
                        while i < j and nums[i] == nums[i - 1]: i += 1
                    elif s > target:
                        j -= 1
                        while i < j and nums[j] == nums[j + 1]: j -= 1
                    else:
                        temp.append([nums[l], nums[i], nums[j],nums[h]])
                        i += 1
                        while i < j and nums[i] == nums[i - 1]: i += 1
                        j -= 1
                        while i < j and nums[j] == nums[j + 1]: j -= 1
        return temp
s = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
t = s.fourSum(nums=nums,target=target)
print(t)

