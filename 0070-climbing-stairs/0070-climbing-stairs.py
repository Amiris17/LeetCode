class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        f_0=1
        f_1=2
        
        
        tmp=0
        
        if n<=2:
            return n
        
        for i in range(n-2):
            tmp=f_0+f_1
            f_0=f_1
            f_1=tmp
            
        return tmp