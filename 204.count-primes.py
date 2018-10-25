#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (27.18%)
# Total Accepted:    186.2K
# Total Submissions: 683.8K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
#
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        '''
        prime_list = [2]

        for i in range(3, n):
            is_p = True
            for p in prime_list:
                if p > i**(0.5):
                    break
                if i%p == 0:
                    is_p = False
                    break
            if is_p:
                prime_list += [i]
        return len(prime_list)
        '''

        count_ls = [1] * n
        count_ls[0], count_ls[1] = 0, 0

        for i in range(2, int(n**0.5)+1):
            if count_ls[i] == 1:
                for j in range(i+i, n, i):
                    count_ls[j] = 0

        return sum(count_ls)
