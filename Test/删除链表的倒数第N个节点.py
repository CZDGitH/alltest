#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = ListNode(-1)
        p.next,a,b = head,p,p
        while n > 0 and a:
            a,n = a.next,n -1
        if not a:
            return head
        while a.next:
            b,a = b.next,a.next
        b.next = b.next.next
        return p.next