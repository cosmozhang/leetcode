#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (41.52%)
# Total Accepted:    305K
# Total Submissions: 734.2K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# But the following [1,2,2,null,3,null,3]  is not:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        l_tree = root.left
        r_tree = root.right

        if self.is_same_tree(l_tree, r_tree):
            return True
        else:
            return False

    def is_same_tree(self, l, r):
        if not l and not r:
            return True
        elif (not l and r != None) or (l != None and not r):
            return False
        else:
            if l.val == r.val:
                return self.is_same_tree(l.left, r.right) and self.is_same_tree(l.right, r.left)
            else:
                return False
