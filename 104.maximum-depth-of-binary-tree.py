#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (57.71%)
# Total Accepted:    410.2K
# Total Submissions: 709.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# return its depth = 3.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root==None:
            return 0
        else:
            if root.left!=None:
                lmax=self.maxDepth(root.left)
            else:
                lmax=0
            if root.right!=None:
                rmax=self.maxDepth(root.right)
            else:
                rmax=0
            return max(lmax, rmax)+1

