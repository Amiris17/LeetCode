class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        sqrt5 = 5**0.5 #BNETS FORMULA
        
      
        
        
        ans = ((1+sqrt5)/2)**(n+1) - ((1-sqrt5)/2)**(n+1)
        
        ans = int(ans/sqrt5)
        
        return ans
    
        
        
    