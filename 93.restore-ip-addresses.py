# -*- coding: utf-8 -*-
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (29.41%)
# Total Accepted:    114.8K
# Total Submissions: 390.5K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
# 
# Example:
# 
# 
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
# 
# 
#
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<4:
            return []

        ret_ls = self.helper(s)

        return ret_ls


    def helper(self, s, l = 4):
        if len(s) == 0:
            return []
        
        if l == 1 and len(s)>=4:
            return []
        elif l == 1 and len(s)<4:
            if len(s) == 1:
                return [s]
            elif len(s) == 2:
                if int(s[0]) != 0:
                    return [s]
                else:
                    return []
            elif len(s) == 3:
                if int(s[0]) != 0 and int(s) <= 255:
                    return [s]
                else:
                    return []


        ret_ls = []
        next_ret = self.helper(s[1:], l-1)
        if next_ret:
            ret_ls += [s[0]+'.'+item for item in next_ret]
            
        if int(s[0]) > 0:
            next_ret = self.helper(s[2:], l-1)
            if next_ret:
                ret_ls += [s[0:2]+'.'+item for item in next_ret]

        if int(s[0]) > 0 and int(s[0:3]) <= 255:
            next_ret = self.helper(s[3:], l-1)
            if next_ret:
                ret_ls += [s[0:3]+'.'+item for item in next_ret]
        
        return ret_ls

