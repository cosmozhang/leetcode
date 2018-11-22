#
# [285] Inorder Successor in BST
#
# https://leetcode.com/problems/inorder-successor-in-bst/description/
#
# algorithms
# Medium (33.11%)
# Total Accepted:    81.8K
# Total Submissions: 246.9K
# Testcase Example:  '[0]\nnode with value 0'
#
# Given a binary search tree and a node in it, find the in-order successor of
# that node in the BST.
# 
# Note: If the given node has no in-order successor in the tree, return null.
# 
# Example 1:
# 
# 
# Input: root = [2,1,3], p = 1
# 
# ⁠ 2
# ⁠/ \
# 1   3
# 
# Output: 2
# 
# Example 2:
# 
# 
# Input: root = [5,3,6,2,4,null,null,1], p = 6
# 
# ⁠     5
# ⁠    / \
# ⁠   3   6
# ⁠  / \
# ⁠ 2   4
# ⁠/   
# 1
# 
# Output: null
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        s = [root]
        node = root
        ret_ls = []
        while s:
            while node:
                node = node.left
                if node:
                    s.append(node)

            node = s.pop(-1)
            ret_ls.append(node.val)
            node = node.right
            if node:
                s.append(node)

        l = 0
        r = len(ret_ls) - 1
        while l <= r:
            m = (l+r) >> 1
            if ret_ls[m] < p.val:
                l = m+1
            elif ret_ls[m] > p.val:
                r = m-1
            else:
                break

        if m == len(ret_ls) - 1:
            return None
        else:
            return ret_ls[m+1]

        




        
