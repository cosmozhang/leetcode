#
# [270] Closest Binary Search Tree Value
#
# https://leetcode.com/problems/closest-binary-search-tree-value/description/
#
# algorithms
# Easy (42.06%)
# Total Accepted:    68.5K
# Total Submissions: 162.8K
# Testcase Example:  '[4,2,5,1,3]\n3.714286'
#
# Given a non-empty binary search tree and a target value, find the value in
# the BST that is closest to the target.
# 
# Note:
# 
# 
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest
# to the target.
# 
# 
# Example:
# 
# 
# Input: root = [4,2,5,1,3], target = 3.714286
# 
# ⁠   4
# ⁠  / \
# ⁠ 2   5
# ⁠/ \
# 1   3
# 
# Output: 4
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        return self.findclosest(root, target, float('inf'), None)
        
    def findclosest(self, node, target, sdiff, bestval):
        if not node:
            return bestval
        elif target == node.val:
            return node.val
        elif target < node.val:
            if abs(node.val-target) < sdiff:
                bestval = node.val
                sdiff = abs(node.val-target)
            return self.findclosest(node.left, target, sdiff, bestval)
        else:
            if abs(node.val-target) < sdiff:
                bestval = node.val
                sdiff = abs(node.val-target)
            return self.findclosest(node.right, target, sdiff, bestval)
