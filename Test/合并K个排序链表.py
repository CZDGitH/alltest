#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
import heapq
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(-1)
        prve = head
        temp = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(temp,(lists[i].val,i))
                lists[i] = lists[i].next
        while temp:
            list,local = heapq.heappop(temp)
            prve.next = ListNode(list)
            prve = prve.next
            if lists[local]:
                heapq.heappush(temp,(lists[local].val,local))
                lists[local] = lists[local].next
        return head.next

