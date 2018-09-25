#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (38.42%)
# Total Accepted:    161.6K
# Total Submissions: 420.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []

        q = [root]
        ret_ls = []
        lvl = 1
        while q:
            new_q = []
            res_this_lvl = []
            for node in q:
                if node:
                    res_this_lvl.append(node.val)
                    if lvl%2 == 1:
                        new_q.append(node.left)
                        new_q.append(node.right)
                    else:
                        new_q.append(node.right)
                        new_q.append(node.left)
            q = new_q[::-1]
            lvl += 1
            if res_this_lvl:
                ret_ls.append(res_this_lvl)

        return ret_ls
            
