class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        remainder_count=0
        while n:
            remainder_count+=n%2
            n=n/2
        return remainder_count
            
       
        