#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (47.87%)
# Total Accepted:    68.5K
# Total Submissions: 143.1K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the
# lists is not allowed.
# 
# 
# 
# Example:
# 
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        s1 = []
        s2 = []

        while l1:
            s1.append(l1)
            l1 = l1.next

        while l2:
            s2.append(l2)
            l2 = l2.next

        t = 0
        old_n = None
        while len(s1) > 0 or len(s2) > 0:
            if len(s1) > 0:
                p = s1.pop(-1)
            else:
                p = ListNode(0)

            if len(s2) > 0:
                q = s2.pop(-1)
            else:
                q = ListNode(0)
            v = p.val + q.val + t
            if v > 9:
                v = v - 10
                t = 1
            else:
                t = 0
            n = ListNode(v)
            n.next = old_n
            old_n = n

        if t == 1:
            head = ListNode(1)
            head.next = old_n
        else:
            head = old_n
        return head
