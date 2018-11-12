#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (40.47%)
# Total Accepted:    72K
# Total Submissions: 177.8K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# 
# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a
# tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
# 
# 
# Example 1:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# 
# Given tree t:
# 
# ⁠  4 
# ⁠ / \
# ⁠1   2
# 
# Return true, because t has the same structure and node values with a subtree
# of s.
# 
# 
# Example 2:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
# 
# Given tree t:
# 
# ⁠  4
# ⁠ / \
# ⁠1   2
# 
# Return false.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        if self.sametree(s, t):
            return True
        
        else:
            if s:
                return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            else:
                return False

    def sametree(self, node, t):

        if not node:
            if not t:
                return True
            else:
                return False
        else:
            if not t:
                return False
            elif node.val != t.val:
                return False
            else:
                return self.sametree(node.left, t.left) and self.sametree(node.right, t.right)
                
