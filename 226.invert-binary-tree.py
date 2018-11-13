#
# [226] Invert Binary Tree
#
# https://leetcode.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (55.62%)
# Total Accepted:    273.7K
# Total Submissions: 491.8K
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# Invert a binary tree.
# 
# Example:
# 
# Input:
# 
# 
# ⁠    4
# ⁠  /   \
# ⁠ 2     7
# ⁠/ \   / \
# 1   3 6   9
# 
# Output:
# 
# 
# ⁠    4
# ⁠  /   \
# ⁠ 7     2
# ⁠/ \   / \
# 9   6 3   1
# 
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
# 
# Google: 90% of our engineers use the software you wrote (Homebrew), but you
# can’t invert a binary tree on a whiteboard so f*** off.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return root

        self.helper(root)

        return root
        
    def helper(self, node):
        if node.left or node.right:
            node.left, node.right = node.right, node.left
            if node.left:
                self.helper(node.left)
            if node.right:
                self.helper(node.right)
            
