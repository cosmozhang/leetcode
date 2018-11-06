#
# [366] Find Leaves of Binary Tree
#
# https://leetcode.com/problems/find-leaves-of-binary-tree/description/
#
# algorithms
# Medium (62.74%)
# Total Accepted:    33.7K
# Total Submissions: 53.7K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a binary tree, collect a tree's nodes as if you were doing this:
# Collect and remove all leaves, repeat until the tree is empty.
# 
# 
# 
# Example:
# 
# 
# Input: [1,2,3,4,5]
# 
# 1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# Output: [[4,5,3],[2],[1]]
# 
# 
# 
# 
# Explanation:
# 
# 1. Removing the leaves [4,5,3] would result in this tree:
# 
# 
# ⁠         1
# ⁠        / 
# ⁠       2          
# 
# 
# 
# 
# 2. Now removing the leaf [2] would result in this tree:
# 
# 
# ⁠         1          
# 
# 
# 
# 
# 3. Now removing the leaf [1] would result in the empty tree:
# 
# 
# ⁠         []         
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret_ls = []
        if not root:
            return ret_ls

        while root and (root.left or root.right):
            leaves = self.find_leaves(root)
            ret_ls += [leaves]

        ret_ls += [[root.val]]

        return ret_ls

    def find_leaves(self, node):

        if not node:
            return []
        
        sub_ret_ls = []

        
        if node.left and not node.left.left and not node.left.right:
            sub_ret_ls += [node.left.val]
            node.left = None
        else:
            left_ret_ls = self.find_leaves(node.left)
            sub_ret_ls += left_ret_ls

        if node.right and not node.right.left and not node.right.right:
            sub_ret_ls += [node.right.val]
            node.right = None
        else:
            right_ret_ls = self.find_leaves(node.right)
            sub_ret_ls += right_ret_ls
        

        return sub_ret_ls
