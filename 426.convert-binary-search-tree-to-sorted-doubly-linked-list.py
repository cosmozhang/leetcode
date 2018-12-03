#
# [758] Convert Binary Search Tree to Sorted Doubly Linked List
#
# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/
#
# algorithms
# Medium (45.12%)
# Total Accepted:    12.7K
# Total Submissions: 28.2K
# Testcase Example:  '{"$id":"1","val":4,"left":{"$id":"2","val":2,"left":{"$id":"4","val":1,"left":null,"right":null},"right":{"$id":"5","val":3,"left":null,"right":null}},"right":{"$id":"3","val":5,"left":null,"right":null}}'
#
# Convert a BST to a sorted circular doubly-linked list in-place. Think of the
# left and right pointers as synonymous to the previous and next pointers in a
# doubly-linked list.
# 
# Let's take the following BST as an example, it may help you understand the
# problem better:
# 
# 
# 
# 
# 
# We want to transform this BST into a circular doubly linked list. Each node
# in a doubly linked list has a predecessor and successor. For a circular
# doubly linked list, the predecessor of the first element is the last element,
# and the successor of the last element is the first element.
# 
# The figure below shows the circular doubly linked list for the BST above. The
# "head" symbol means the node it points to is the smallest element of the
# linked list.
# 
# 
# 
# 
# 
# Specifically, we want to do the transformation in place. After the
# transformation, the left pointer of the tree node should point to its
# predecessor, and the right pointer should point to its successor. We should
# return the pointer to the first element of the linked list.
# 
# The figure below shows the transformed BST. The solid line indicates the
# successor relationship, while the dashed line means the predecessor
# relationship.
# 
# 
# 
# 
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if not root:
            return None

        head, tail = self.helper(root)

        head.left = tail
        tail.right = head

        return head

    def helper(self, node):

        lhead, rtail = node, node
        if node.left:
            lhead, ltail = self.helper(node.left)
            ltail.right = node
            node.left = ltail
        if node.right:
            rhead, rtail = self.helper(node.right)
            rhead.left = node
            node.right = rhead
        lhead.left = None
        rtail.right = None

        return lhead, rtail
        
