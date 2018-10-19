#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (34.17%)
# Total Accepted:    246.1K
# Total Submissions: 720K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
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
# return its minimum depth = 2.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return self.helper(root)
    
    def helper(self, node):

        if not node.left and not node.right:
            return 1
        elif node.left and not node.right:
            return self.helper(node.left)+1
        elif not node.left and node.right:
            return self.helper(node.right)+1
        else:
            return min(self.helper(node.left), self.helper(node.right))+1
