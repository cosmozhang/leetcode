#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (48.20%)
# Total Accepted:    178.3K
# Total Submissions: 370K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# Given a binary search tree, write a function kthSmallest to find the kth
# smallest element in it.
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
# 
# Example 1:
# 
# 
# Input: root = [3,1,4,null,2], k = 1
# ⁠  3
# ⁠ / \
# ⁠1   4
# ⁠ \
# 2
# Output: 1
# 
# Example 2:
# 
# 
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# ⁠      5
# ⁠     / \
# ⁠    3   6
# ⁠   / \
# ⁠  2   4
# ⁠ /
# ⁠1
# Output: 3
# 
# 
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to
# find the kth smallest frequently? How would you optimize the kthSmallest
# routine?
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root.left and k == 1:
            return root.val
        
        if root.left:
            l = self.helper(root.left)
            if k == l + 1:
                return root.val
            elif k <= l:
                return self.kthSmallest(root.left, k)
            elif k > l+1:
                return self.kthSmallest(root.right, k-l-1)
        else:
            return self.kthSmallest(root.right, k-1)   


    def helper(self, node):
        # return num of nodes under this node, including itself
        if not node.left and not node.right:
            return 1
        elif node.left and not node.right:
            return 1 + self.helper(node.left)
        elif node.right and not node.left:
            return 1 + self.helper(node.right)
        else:
            return self.helper(node.left) + self.helper(node.right) + 1
