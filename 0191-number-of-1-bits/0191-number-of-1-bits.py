class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        remainder_count=0
        while n:
            remainder_count+=n%2 #0 wont matter we just get all 1's 
            n=n>>1
        return remainder_count
            
       
        