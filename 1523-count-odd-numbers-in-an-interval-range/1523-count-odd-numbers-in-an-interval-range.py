class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        
        if(high%2==0 and low%2==0):
            return (high-low)/2
        else:
            return ((high-low)/2) +1
        
        
        

        
        "remember coutn of odd numbers  =n/2+"