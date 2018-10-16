#
# [166] Fraction to Recurring Decimal
#
# https://leetcode.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (18.59%)
# Total Accepted:    74.2K
# Total Submissions: 399K
# Testcase Example:  '1\n2'
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
# 
# If the fractional part is repeating, enclose the repeating part in
# parentheses.
# 
# Example 1:
# 
# 
# Input: numerator = 1, denominator = 2
# Output: "0.5"
# 
# 
# Example 2:
# 
# 
# Input: numerator = 2, denominator = 1
# Output: "2"
# 
# Example 3:
# 
# 
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
# 
# 
#
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == '0':
            return ''

        if numerator == '0':
            return '0'
        
        if numerator * denominator >= 0:
            sign = ''
        else:
            sign = '-'

        num = abs(numerator)
        den = abs(denominator)

        if num % den == 0:
            bd = str(num/den)
            return sign+bd
        else:
            bd = str(num/den)
            rem = num % den

        ad = '.'
        c = 0
        rem_dic = {}
        f = False
        while rem!=0:
            c += 1
            if rem in rem_dic:
                f = True
                l = rem_dic[rem]
                break
            rem_dic[rem] = c
            rem = rem*10
            ad += str(rem/den)
            rem = rem%den

        if f:
            ad = ad[:l]+'('+ad[l:]+')'

        return sign + bd + ad
        

'''
if __name__ == '__main__':
    s = Solution()
    print s.fractionToDecimal(0, 3)
'''
