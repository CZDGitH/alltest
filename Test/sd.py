from time import time
from typing import List
# import numpy as np
start = time()
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            nums1,nums2 = nums2,nums1
            m,n = n,m
        imin,imax = 0,m
        harfLen = (m + n + 1)//2
        while imin <= imax:
            i = (imin + imax)//2
            j = harfLen - i
            if i > imin and nums1[i - 1] > nums2[j]:
                imax = i - 1
            elif i < imax and nums2[j - 1] > nums1[i]:
                imin = i + 1
            else:
                if i == 0:maxLeft = nums2[j - 1]
                elif j == 0:maxLeft = nums1[i - 1]
                else:maxLeft = max(nums1[i - 1],nums2[j - 1])

                if (m + n)%2 == 1:return maxLeft

                if i == m:minRight = nums2[j]
                elif j == n:minRight = nums1[i]
                else:minRight = min(nums1[i],nums2[j])

                return (maxLeft + minRight)/2
        return 0.0
    #########################################



g = Solution()
a1 = [1,3]
a2 = [2]
s = g.findMedianSortedArrays(nums1=a1,nums2=a2)

g = 'abca'
print(3//2)
print(time()-start)
for i in range(len(g)):
    print(i)

print('````````````````')
tempS = [1]
print(tempS[0])
