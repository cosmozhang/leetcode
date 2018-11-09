#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (34.41%)
# Total Accepted:    203.1K
# Total Submissions: 589.8K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return True

        l = head
        r = head

        while r.next:

            r = r.next

            if r.next:
                r = r.next
            else:
                break
            l = l.next

        n_h = l.next
        l.next = None

        old = None
        while n_h:
            t = n_h
            n_h = n_h.next
            t.next = old
            old = t

        while t:
            if t.val == head.val:
                t = t.next
                head = head.next
            else:
                return False

        return True

        

        
