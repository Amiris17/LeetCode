class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        remainder_count=0
        while n:
            n&=(n-1)
            remainder_count+=1
        return remainder_count
            
       
        