#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (28.51%)
# Total Accepted:    553.6K
# Total Submissions: 1.9M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
    # def __init__(self, x):
        # self.val = x
        # self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        to_return = l3
        while l1 != None or l2 != None:
            if l1 == None:
                l1 = ListNode(0)
            if l2 == None:
                l2 = ListNode(0)
            if l1.next != None or l2.next != None:
                l3.next = ListNode(0)
            s = l1.val + l2.val + l3.val
            if s >= 10:
                l3.next = ListNode(1)
                l3.val = s-10
            else:
                l3.val = s
            l1, l2 = l1.next, l2.next
            l3 = l3.next
        return to_return
            
        
