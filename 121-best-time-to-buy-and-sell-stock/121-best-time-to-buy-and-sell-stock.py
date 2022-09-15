class Solution(object):
    def maxProfit(self, s):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        
        
        
        
        
        #buy < sell
        buy=s[0]
        sell=0
        profit=0
        
        for i in range(len(s)):
            if s[i]<buy:
                buy=s[i]
                
            elif s[i]-buy>profit:
                profit=s[i]-buy
                
        return profit
        
        
       
    
    