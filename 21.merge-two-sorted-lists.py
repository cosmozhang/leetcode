#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (43.45%)
# Total Accepted:    423.3K
# Total Submissions: 973.4K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        if not l1 and l2:
            return l2
        if not l2 and l1:
            return l1
        
        dummy_head = ListNode(None)

        node = dummy_head
        node1 = l1
        node2 = l2
        while True:
            if node1.val <= node2.val:
                node.next = node1
                node1 = node1.next
                node = node.next
                if not node1:
                    node.next = node2
                    break
            else:
                node.next = node2
                node2 = node2.next
                node = node.next
                if not node2:
                    node.next = node1
                    break

        return dummy_head.next
