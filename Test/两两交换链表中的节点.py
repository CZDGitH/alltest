#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        temp = head.next
        head.next = self.swapPairs(temp.next)
        temp.next = head
        return temp