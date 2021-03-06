#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (48.55%)
# Total Accepted:    267.9K
# Total Submissions: 550.1K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,2,3]
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        res_ls = []
        stack = [root]
        while stack:
            node = stack.pop(-1)
            res_ls.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res_ls
