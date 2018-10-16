#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (44.59%)
# Total Accepted:    129.4K
# Total Submissions: 290.1K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# 
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        row_ls = []
        s = [root]
        while s:
            new_s = []
            row_res = []
            for node in s:
                row_res.append(node.val)
                if node.left:
                    new_s.append(node.left)
                if node.right:
                    new_s.append(node.right)
            row_ls += [row_res]
            s = new_s
        ret_ls = [row[-1] for row in row_ls]
        return ret_ls
