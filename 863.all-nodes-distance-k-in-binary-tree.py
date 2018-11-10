#
# [893] All Nodes Distance K in Binary Tree
#
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
#
# algorithms
# Medium (43.11%)
# Total Accepted:    10.9K
# Total Submissions: 25.2K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
#
# We are given a binary tree (with root node root), a target node, and an
# integer value K.
# 
# Return a list of the values of all nodes that have a distance K from the
# target node.  The answer can be returned in any order.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# 
# Output: [7,4,1]
# 
# Explanation: 
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
# 
# 
# 
# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these
# objects.
# 
# 
# 
# 
# Note:
# 
# 
# The given tree is non-empty.
# Each node in the tree has unique values 0 <= node.val <= 500.
# The target node is a node in the tree.
# 0 <= K <= 1000.
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
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if K == 0:
            return [target.val]
        
        self.convert_to_linked_ls(root, None)
        
        q= set([target])
        visited = set()
        while len(q) != 0:
            new_q = set()
            for node in q:
                visited.add(node)
                for neibour in node.neibours:
                    if neibour not in visited:
                        new_q.add(neibour)
            K -= 1
            q = new_q
            if K == 0:
                break
            
        if K == 0:
            return [n.val for n in new_q]
        else:
            return []
                

    def convert_to_linked_ls(self, node, parent):

        if node:
            if parent:
                node.neibours = [parent]
            else:
                node.neibours = []
                
            if node.left:
                node.neibours.append(node.left)
                self.convert_to_linked_ls(node.left, node)

            if node.right:
                node.neibours.append(node.right)
                self.convert_to_linked_ls(node.right, node)
        

        
