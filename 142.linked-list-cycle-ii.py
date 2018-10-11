#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (29.95%)
# Total Accepted:    172K
# Total Submissions: 575.1K
# Testcase Example:  '[]\nno cycle'
#
# 
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
# 
# 
# 
# Note: Do not modify the linked list.
# 
# 
# Follow up:
# Can you solve it without using extra space?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy_head = ListNode(None)
        dummy_head.next = head
        l, r = dummy_head.next, dummy_head.next
        if not r:
            return None

        is_cycle = False
        while r:
            l = l.next
            r = r.next
            if not r:
                return None
            else:
                r = r.next
            if l == r:
                is_cycle = True
                break
        if not is_cycle:
            return None
        else:
            l = dummy_head.next
            while l != r:
                l, r = l.next, r.next
            return l
