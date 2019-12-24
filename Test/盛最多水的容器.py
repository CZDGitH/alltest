#!/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPoint = 0
        rightPoint = len(height) - 1
        maxArea = 0
        while leftPoint < rightPoint:
            tempArea = (rightPoint - leftPoint)*min(height[leftPoint],height[rightPoint])
            if tempArea > maxArea : maxArea = tempArea
            if height[leftPoint] <= height[rightPoint]:
                i = 1
                while height[leftPoint] >= height[leftPoint + i]:
                    i += 1
                    if leftPoint + i >= rightPoint:return maxArea
                leftPoint = leftPoint + i
            else:
                j = 1
                while height[rightPoint] >= height[rightPoint - j]:
                    j += 1
                    if rightPoint - j <= leftPoint:return maxArea
                rightPoint = rightPoint - j
        return maxArea

t = Solution()
heightList = [0,2]
area = t.maxArea(height = heightList)
print(area)



