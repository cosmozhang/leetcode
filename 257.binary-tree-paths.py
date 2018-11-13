#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (43.70%)
# Total Accepted:    192.1K
# Total Submissions: 439.6K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# Output: ["1->2->5", "1->3"]
# 
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = self.helper(root)

        str_ret = []
        for path in paths:
            str_path = '->'.join([str(v) for v in path])
            str_ret.append(str_path)

        return str_ret
        

    def helper(self, node):
        if not node:
            return []
        elif not node.left and not node.right:
            return [[node.val]]
        else:
            res_ls = []
            if node.left:
                left_ret = self.helper(node.left)
                for ls in left_ret:
                    res_ls.append([node.val] + ls)
            if node.right:
                right_ret = self.helper(node.right)
                for ls in right_ret:
                    res_ls.append([node.val] + ls)
            return res_ls
