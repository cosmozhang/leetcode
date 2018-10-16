#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (34.19%)
# Total Accepted:    106.8K
# Total Submissions: 312.3K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to
# identify repeated sequences within the DNA.
# 
# Write a function to find all the 10-letter-long sequences (substrings) that
# occur more than once in a DNA molecule.
# 
# Example:
# 
# 
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]
# 
# 
#
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        dna_dic = {}
        ret_ls = []
        l = range(len(s)-10+1)
        for i in l:
            c = s[i:i+10]
            if c in dna_dic and dna_dic[c] == 0:
                ret_ls += [c]
                dna_dic[c] = 1
            elif c not in dna_dic:
                dna_dic[c] = 0
        return ret_ls
                
