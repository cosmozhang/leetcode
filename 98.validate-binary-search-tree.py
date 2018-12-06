#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (24.43%)
# Total Accepted:    286.9K
# Total Submissions: 1.2M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# Example 1:
# 
# 
# Input:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# Output: true
# 
# 
# Example 2:
# 
# 
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# Output: false
# Explanation: The input is: [5,1,4,null,null,3,6]. The root node's
# value
# is 5 but its right child's value is 4.
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
    '''
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.helper(root, float("inf"), float("-inf"))

    def helper(self, node, max_v, min_v):
        if not node:
            return True
        
        left_res = True
        if node.left:
            if node.left.val >= node.val or node.left.val <= min_v or not self.helper(node.left, node.val, min_v): # all nodes below should be smaller than this node
                left_res = False
        
        right_res = True
        if node.right:
            if node.right.val <= node.val or node.right.val >= max_v or not self.helper(node.right, max_v, node.val): # all nodes below should be larger than this node
                right_res = False

        if left_res and right_res:
            return True
        else:
            return False

    '''
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, node, min_v, max_v):
        if not node:
            return True

        else:
            if min_v < node.val and node.val < max_v:
                
                return self.helper(node.left, min_v, node.val) and self.helper(node.right, node.val, max_v)
            else:
                return False
        
