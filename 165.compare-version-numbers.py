#
# [165] Compare Version Numbers
#
# https://leetcode.com/problems/compare-version-numbers/description/
#
# algorithms
# Medium (21.65%)
# Total Accepted:    113.4K
# Total Submissions: 523.6K
# Testcase Example:  '"0.1"\n"1.1"'
#
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise
# return 0.
# 
# You may assume that the version strings are non-empty and contain only digits
# and the . character.
# The . character does not represent a decimal point and is used to separate
# number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it
# is the fifth second-level revision of the second first-level revision.
# 
# Example 1:
# 
# 
# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
# 
# Example 2:
# 
# 
# Input: version1 = "1.0.1", version2 = "1"
# Output: 1
# 
# Example 3:
# 
# 
# Input: version1 = "7.5.2.4", version2 = "7.5.3"
# Output: -1
# 
#
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')

        while v1 or v2:
            x = v1.pop(0)
            y = v2.pop(0)
            if int(x)>int(y):
                return 1
            elif int(x)<int(y):
                return -1
            elif int(x)==int(y):
                if not v2 and not v1:
                    return 0
                elif not v1 and v2:
                    while v2:
                        z = v2.pop(0)
                        if int(z)>0:
                            return -1
                    return 0
                elif v1 and not v2:
                    while v1:
                        z = v1.pop(0)
                        if int(z)>0:
                            return 1
                    return 0
                
