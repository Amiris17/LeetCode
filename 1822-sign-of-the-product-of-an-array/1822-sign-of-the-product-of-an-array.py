class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        neg=0
        pos=0
         #"1 for multiplication not 0"
        for i in nums:
            if i<0:
                neg+=1
            if i>0:
                pos+=1
        
            if i==0:
                return 0
        if neg%2==0:
            return 1
        else:
            return -1
            
            
        
        

    
        
        
        
        
            