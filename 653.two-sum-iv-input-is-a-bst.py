#
# [653] Two Sum IV - Input is a BST
#
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (51.07%)
# Total Accepted:    62.5K
# Total Submissions: 122.3K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# Given a Binary Search Tree and a target number, return true if there exist
# two elements in the BST such that their sum is equal to the given target.
#
# Example 1:
#
# Input:
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Target = 9
#
# Output: True
#
#
#
#
# Example 2:
#
# Input:
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Target = 28
#
# Output: False
#
#
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
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.root = root
        return self.helper(root, k)

    def helper(self, node, k):

        if not node:
            return False

        m = k - node.val
        if m != node.val:
            n = self.root
            while n:
                if m == n.val:
                    return True
                elif m < n.val:
                    n = n.left
                else:
                    n = n.right
        return self.helper(node.left, k) or self.helper(node.right, k)

