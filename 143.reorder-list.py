#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (28.14%)
# Total Accepted:    127.1K
# Total Submissions: 449.5K
# Testcase Example:  '[1,2,3,4]'
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# Example 1:
# 
# 
# Given 1->2->3->4, reorder it to 1->4->2->3.
# 
# Example 2:
# 
# 
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        '''
        dummy_head = ListNode(None)
        dummy_head.next = head
        id2node_dic = {}
        i = 0
        while head:
            id2node_dic[i] = head
            head = head.next
            if head:
                i += 1

        n = i
        j = 0
        node = dummy_head.next
        while j < n/2:
            tmp = node.next
            node.next = id2node_dic[n-j]
            node.next.next = tmp
            node = tmp
            j += 1
        if n == 0:
            pass
        elif n%2 == 1:
            node.next.next = None
        else:
            node.next = None
        '''

        if head and head.next:

            l = head
            r = head
            while True:
                if r.next:
                    r = r.next
                else:
                    s_head = l.next
                    l.next = None
                    break
            
                if r.next:
                    r = r.next
                else:
                    s_head = l.next
                    l.next = None
                    break
                l = l.next

            old = None
            while s_head:
                n = s_head.next
                s_head.next = old
                old = s_head
                s_head = n

            s_head = old
            node = head

            while s_head:
                n = s_head.next
                t = node.next
                node.next = s_head
                node.next.next = t
                s_head = n
                node = t
