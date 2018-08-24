#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (40.29%)
# Total Accepted:    232.1K
# Total Submissions: 574.9K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# Note:
# 
# 
# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next ==None:
            return head
        l = head
        r = head.next
        l.next = r.next
        r.next = l
        l, r = r, l
        tail = r
        head = l
        while l.next.next and r.next.next:
            l = l.next.next
            r = r.next.next
            l.next = r.next
            r.next = l
            tail.next = r
            l, r = r, l
            tail = r
        
            
        return head
