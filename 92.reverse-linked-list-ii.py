#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (32.50%)
# Total Accepted:    155.3K
# Total Submissions: 477.8K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m == n:
            return head

        j = 0
        dummy_head = ListNode(None)
        dummy_head.next = head
        bridging_tail = dummy_head
        l, r = dummy_head, head
        while True:
            if r:
                temp = r.next
            if j == m-1:
                bridging_tail = l
                mid_tail = r
            elif m <= j and j < n:
                r.next = l
            elif j == n:
                mid_head = l
                bridging_head = r
            elif j > n:
                break
            if not r:
                break
            j += 1
            l, r = r, temp

        bridging_tail.next = mid_head
        mid_tail.next = bridging_head
        
        return dummy_head.next
            
            
