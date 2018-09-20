#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (30.66%)
# Total Accepted:    149.5K
# Total Submissions: 483K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# 
# Example 1:
# 
# 
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# 
# 
# Example 2:
# 
# 
# Input: 1->1->1->2->3
# Output: 2->3
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        dummy_head = ListNode(None)
        dummy_head.next = head
        l = dummy_head
        r = l.next

        while r.next:
            if r.next.val == r.val:
                c = r.val
                while True:
                    r = r.next
                    if not r or r.val != c:
                        break
                l.next = r
                if not r:
                    break
            else:
                l = l.next
                r = r.next
                
        return dummy_head.next
