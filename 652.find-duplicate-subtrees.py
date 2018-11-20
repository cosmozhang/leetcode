#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (41.63%)
# Total Accepted:    25.5K
# Total Submissions: 61.3K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# Given a binary tree, return all duplicate subtrees. For each kind of
# duplicate subtrees, you only need to return the root node of any one of
# them.
# 
# Two trees are duplicate if they have the same structure with same node
# values.
# 
# Example 1: 
# 
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
# 
# 
# The following are two duplicate subtrees:
# 
# 
# ⁠     2
# ⁠    /
# ⁠   4
# 
# 
# and
# 
# 
# ⁠   4
# 
# Therefore, you need to return above trees' root in the form of a list.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        
        pattern_dic = {}

        self.helper(root, pattern_dic)

        ret_ls = []
        for k, v in pattern_dic.iteritems():
            if v[0] > 1:
                ret_ls.append(v[1])

        return ret_ls

    def helper(self, node, p_dic):
        if not node:
            return '#'

        p = str(node.val) + ',' + self.helper(node.left, p_dic) + ',' + self.helper(node.right, p_dic)

        if p not in p_dic:
            p_dic[p] = [1, node]
        else:
            p_dic[p][0] += 1

        return p
