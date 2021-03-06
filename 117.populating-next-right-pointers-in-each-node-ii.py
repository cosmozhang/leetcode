#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (33.52%)
# Total Accepted:    149.2K
# Total Submissions: 445K
# Testcase Example:  '{}'
#
# Given a binary tree
# 
# 
# struct TreeLinkNode {
# ⁠ TreeLinkNode *left;
# ⁠ TreeLinkNode *right;
# ⁠ TreeLinkNode *next;
# }
# 
# 
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# Note:
# 
# 
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra
# space for this problem.
# 
# 
# Example:
# 
# Given the following binary tree,
# 
# 
# ⁠    1
# ⁠  /  \
# ⁠ 2    3
# ⁠/ \    \
# 4   5    7
# 
# 
# After calling your function, the tree should look like:
# 
# 
# ⁠    1 -> NULL
# ⁠  /  \
# ⁠ 2 -> 3 -> NULL
# ⁠/ \    \
# 4-> 5 -> 7 -> NULL
# 
# 
#
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        dummy = TreeLinkNode(-1)
        node = dummy
        while root:
            while root:
                if root.left:
                    node.next = root.left
                    node = node.next
                if root.right:
                    node.next = root.right
                    node = node.next
                root = root.next
            root= dummy.next
            node = dummy
            node.next = None
