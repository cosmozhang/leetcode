#
# [799] Minimum Distance Between BST Nodes
#
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (48.63%)
# Total Accepted:    20K
# Total Submissions: 41.1K
# Testcase Example:  '[4,2,6,1,3,null,null]'
#
# Given a Binary Search Tree (BST) with the root node root, return the minimum
# difference between the values of any two different nodes in the tree.
# 
# Example :
# 
# 
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.
# 
# The given tree [4,2,6,1,3,null,null] is represented by the following
# diagram:
# 
# ⁠         4
# ⁠       /   \
# ⁠     2      6
# ⁠    / \    
# ⁠   1   3  
# 
# while the minimum difference in this tree is 1, it occurs between node 1 and
# node 2, also between node 3 and node 2.
# 
# 
# Note:
# 
# 
# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's
# value is different.
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
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = self.find(root)

        return ret[0]

    def find(self, node):

        if not node:
            return None
        else:
            l_ret = self.find(node.left)
            if l_ret:
                l_min_diff = min(l_ret[0], node.val - l_ret[2])
            else:
                l_min_diff = float('inf')

            r_ret = self.find(node.right)
            if r_ret:
                r_min_diff = min(r_ret[0], r_ret[1] - node.val)
            else:
                r_min_diff = float('inf')

            v_l = l_ret[1] if l_ret else node.val #min v in left
            v_r = r_ret[2] if r_ret else node.val #max v in right

            return (min(l_min_diff, r_min_diff), v_l, v_r)
            

