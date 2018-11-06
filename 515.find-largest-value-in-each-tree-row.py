#
# [515] Find Largest Value in Each Tree Row
#
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (56.36%)
# Total Accepted:    51.3K
# Total Submissions: 90.9K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# You need to find the largest value in each row of a binary tree.
# 
# Example:
# 
# Input: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \  
# ⁠     5   3   9 
# 
# Output: [1, 3, 9]
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
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        
        ret_ls = []
        if not root:
            return ret_ls

        cur_q = [root]

        while cur_q:
            ret_ls += [max([node.val for node in cur_q])]
            new_q = []
            for node in cur_q:
                if node.left:
                    new_q += [node.left]
                if node.right:
                    new_q += [node.right]
            cur_q = new_q

        return ret_ls
                            

        
