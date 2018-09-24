#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (33.28%)
# Total Accepted:    113.3K
# Total Submissions: 340.4K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
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
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        
        ret_ls = self.helper(1, n)
        return ret_ls

    def helper(self, i, j):
        if i > j:
            return [None]

        ret_ls = []
        for k in range(i, j+1):
            ltrees = self.helper(i, k-1)
            rtrees = self.helper(k+1, j)
            for ltree in ltrees:
                for rtree in rtrees:
                    k_node = TreeNode(k)
                    k_node.left = ltree
                    k_node.right = rtree
                    ret_ls.append(k_node)
        return ret_ls
