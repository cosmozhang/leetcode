#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (28.21%)
# Total Accepted:    228.2K
# Total Submissions: 808.8K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#
#
# string convert(string s, int numRows);
#
# Example 1:
#
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
#
# Example 2:
#
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        else:
            ls = [[] for i in range(numRows)]
            for row_number in range(numRows):
                gap_ls = [i*2 for i in range(numRows)]
                gap_ls[0] = gap_ls[-1]
                gap_ls = gap_ls[::-1]
                idx = row_number
                while idx < len(s):
                    ls[row_number].append(s[idx])
                    idx += gap_ls[row_number]
                    gap_ls = gap_ls[::-1]
            c_ls = []
            for row_ls in ls:
                c_ls += row_ls
            new_s = ''.join(c_ls)
            return new_s

