#!/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) <=3:return sum(nums)
        nums.sort()
        if sum(nums[0:3]) >= target:return sum(nums[0:3])
        temp = sum(nums[0:3])
        for l in range(len(nums) - 2):
            if sum(nums[l:l+3]) >= target:
                if (abs(temp - target) - abs(sum(nums[l:l+3]) - target)) > 0:return sum(nums[l:l+3])
                else:return temp
            elif (l > 0 and nums[l] == nums[l - 1]):continue
            i,j = l + 1,len(nums) - 1
            while i < j:
                s = nums[l] + nums[i] + nums[j]
                if s < target:
                    if (abs(temp - target) - abs(s - target)) > 0:
                        temp = s
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif s > target:
                    if (abs(temp - target) - abs(s - target)) > 0:
                        temp = s
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    return s
        return temp

s = Solution()
nums = [6,-18,-20,-7,-15,9,18,10,1,-20,-17,-19,-3,-5,-19,10,6,-11,1,-17,-15,6,17,-18,-3,16,19,-20,-3,-17,-15,-3,12,1,-9,4,1,12,-2,14,4,-4,19,-20,6,0,-19,18,14,1,-15,-5,14,12,-4,0,-10,6,6,-6,20,-8,-6,5,0,3,10,7,-2,17,20,12,19,-13,-1,10,-1,14,0,7,-3,10,14,14,11,0,-4,-15,-8,3,2,-5,9,10,16,-4,-3,-9,-8,-14,10,6,2,-12,-7,-16,-6,10]
target = -52
t = s.threeSumClosest(nums=nums,target=target)
print(t)
