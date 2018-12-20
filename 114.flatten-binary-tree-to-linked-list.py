#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (38.63%)
# Total Accepted:    189.3K
# Total Submissions: 490K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example, given the following tree:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 
# The flattened tree should look like:
# 
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        
        ls = []
        self.helper(root, ls)
        root.left = None
        node = root
        if ls:
            for v in ls[1:]:
                node.right = TreeNode(v)
                node = node.right
                
    
    def helper(self, node, ls):
        if node:
            ls.append(node.val)
            self.helper(node.left, ls)
            self.helper(node.right, ls)
'''
class Solution(object):
    def flatten(self, root):
        ''''
        tmp_ls = []
        while root:
            if root.left:
                if root.right:
                    tmp_ls.append(root.right)
                root.right = root.left
                root.left = None
            else:
                if root.right:
                   pass 
                else:
                    if tmp_ls:
                        node = tmp_ls.pop()
                        root.right = node
            root = root.right
        '''
        if root:
            self.helper(root)
        
    def helper(self, node):

        h, t = node, node
        l, r = node.left, node.right
        if l:
            l_h, l_t = self.helper(l)
            t.right = l_h
            t = l_t
        if r:
            r_h, r_t = self.helper(r)
            t.right = r_h
            t = r_t
            
        h.left = None
        return h, t
        
                    
        
