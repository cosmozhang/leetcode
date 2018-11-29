#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (34.63%)
# Total Accepted:    300.7K
# Total Submissions: 868.3K
# Testcase Example:  '[]\nno cycle'
#
# 
# Given a linked list, determine if it has a cycle in it.
# 
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
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        node1 = head
        node2 = head

        while node1 is not None and node2 is not None:

            node1 = node1.next

            node2 = node2.next

            if node2 is None:
                return False
            node2 = node2.next

            if  node1 == node2:
                return True

        return False
