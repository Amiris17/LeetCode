class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #
        
        bin_n=bin(n)
        
        str_n=str(bin_n)
        
        print(str_n)
        
        count=0
        
        for i in str_n:
            print(i)
            if i=="1":
                count+=1
                
        return count
            
            
        #while we could convert it back to a 32 signed for our answer it doesnt matter
        
        
        