class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        
        s=0
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                s = s + sum(arr[i:j+1])
        return s
    
    
            
        #1,2,3
        #
        
        