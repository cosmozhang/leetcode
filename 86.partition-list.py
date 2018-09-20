#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (34.41%)
# Total Accepted:    136.1K
# Total Submissions: 391.6K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# Example:
# 
# 
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return head

        left_dummy_head = ListNode(None)
        right_dummy_head = ListNode(None)

        l = left_dummy_head
        r = right_dummy_head
        c = head
        while c:
            if c.val < x:
                l.next = ListNode(c.val)
                l = l.next
            else:
                r.next = ListNode(c.val)
                r = r.next
            c = c.next
        l.next = right_dummy_head.next

        return left_dummy_head.next
                
            
