#
# [449] Serialize and Deserialize BST
#
# https://leetcode.com/problems/serialize-and-deserialize-bst/description/
#
# algorithms
# Medium (44.26%)
# Total Accepted:    40.6K
# Total Submissions: 91.8K
# Testcase Example:  '[2,1,3]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment. 
# 
# Design an algorithm to serialize and deserialize a binary search tree. There
# is no restriction on how your serialization/deserialization algorithm should
# work. You just need to ensure that a binary search tree can be serialized to
# a string and this string can be deserialized to the original tree
# structure.
# 
# 
# The encoded string should be as compact as possible.
# 
# 
# 
# Note: Do not use class member/global/static variables to store states. Your
# serialize and deserialize algorithms should be stateless.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        
        s = [root]
        ret_ls = []
        while len(s) > 0:
            node = s.pop(0)
            if node:
                ret_ls.append(str(node.val)+'\t')
                s.append(node.left)
                s.append(node.right)
            else:
                ret_ls.append('n\t')
        return ''.join(ret_ls)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        
        dl = list(data.rstrip('\t').split('\t'))
        root_val = dl.pop(0)
        root = TreeNode(root_val)
        q = [root]
        lrc = 0
        while len(dl)>0:
            n_v = dl.pop(0)
            if lrc%2 == 0:
                node = q.pop(0)
                if n_v != 'n':
                    node.left = TreeNode(int(n_v))
                    q.append(node.left)
                else:
                    node.left = None
            else:
                if n_v != 'n':
                    node.right = TreeNode(int(n_v))
                    q.append(node.right)
                else:
                    node.right = None
            lrc += 1
            
        return root
            
        

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
