"""
https://leetcode.com/submissions/detail/147677024/

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

Credits:Special thanks to @ts for adding this problem and creating all test cases."""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = '{0:b}'.format(n)
        count = 0
        for letter in binary:
            if letter == '1':
                count += 1
        return count
        